# Introduction
rewrite from https://github.com/Acly/comfyui-tooling-nodes
* but support more big data
* can receive batch imgs
* can send batch imgs much more than 4MB

# How I use it to send batch imgs
```python
def _is_continuous(self, img_data):
    keys = sorted(img_data.keys())
    return keys == list(range(len(keys)))
def _merge_base64_to_pil(self, allb64):
    result = {}
    for node, node_data in allb64.items():
        result[node] = []
        for img_index, img_data in node_data.items():
            if not self._is_continuous(img_data):
                print(
                    f"Skipping non-continuous image: node_{node}_image_{img_index}"
                )
                continue

            full_b64 = "".join(value for _, value in sorted(img_data.items()))

            try:
                img_bytes = base64.b64decode(full_b64)
                img = Image.open(io.BytesIO(img_bytes))
                result[node].append(img)
                logger.info(f"Processed image: node_{node}_image_{img_index}")
            except Exception as e:
                logger.error(
                    f"Error processing image: node_{node}_image_{img_index}. Error: {str(e)}"
                )

    return result

async def _get_images(self, ws, prompt, client_id):
    prompt_id = (await self._queue_prompt(prompt, client_id))["prompt_id"]

    allb64 = {}
    try:
        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                message = json.loads(msg.data)
                if message["type"] == "progress" and message.get("data"):
                    pass
                if message["type"] == "executing" and message.get("data"):
                    data = message["data"]
                    if data["node"] is None and data["prompt_id"] == prompt_id:
                        break
                if message["type"] == "ntlb64part" and message.get("data"):
                    mdata = message["data"]
                    nodelabel = mdata["nodelabel"]
                    img_idx = mdata["img_idx"]
                    part_idx = mdata["part_idx"]
                    part_b64 = mdata["part_b64"]
                    if nodelabel not in allb64:
                        allb64[nodelabel] = {}
                        pass
                    if img_idx not in allb64[nodelabel]:
                        allb64[nodelabel][img_idx] = {}
                        pass
                    allb64[nodelabel][img_idx][part_idx] = part_b64
                    pass
    except aiohttp.ClientError as ex:
        raise Exception("WebSocket error: " + str(ex))

    output_images = self._merge_base64_to_pil(allb64)
    return output_images

@asynccontextmanager
async def websocket_connect(url):
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect(url) as ws:
            try:
                yield ws
            except aiohttp.ClientError as ex:
                raise Exception("WebSocket connection error: " + str(ex))

async with websocket_connect(url) as ws:
    node_outputs = await self._get_images(ws, drawconfig, self._client_id)
    images = fetchImgsFromNode(outputpath, node_outputs, ftype=2)

```
