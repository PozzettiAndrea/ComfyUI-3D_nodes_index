# ComfyUI-MDNotes

该自定义节点可根据checkpoints / lora名称自动寻找对应的markdown笔记文件并呈现给用户；用户在编辑器中完成修改后，可回存至硬盘中。

Find, display and save markdown notes from/to hard drive of checkpoints and loras according to the name of them.

## 概述 - Overview

ComfyUI-MDNotes在CheckpointLoader等节点上注册了Show note of checkpoint、Show note of lora、Show note of unet 等右键菜单。在这些节点上右键即可看到这些菜单，点击上述菜单选项即会弹出如下对话框，用户可随意读取/修改笔记文件。

ComfyUI-MDNotes registers new right-click menu items for nodes including CheckpointLoader. Three menu items ("Show note of checkpoint", "Show note of lora" and "Show note of unet") are added when right clicking those nodes. Clicking on these menu items will open a dialog box where users can read and edit the corresponding markdown notes.

![image1](doc/image.png)

## 技术栈 - Technology Stack

- [Vue.js](https://vuejs.org/) - 超棒的JavaScript框架 (A fascinating JavaScript framework)
- [Vditor](https://b3log.org/vditor/) - 所见即所得的markdown编辑器 (A WYSIWYG markdown editor)
- [PrimeVue](https://primevue.org/) - ComfyUI原生提供的前端UI组件库 (A front-end UI component library provided by ComfyUI)
- [PrimeVue Icons]([https://icons.getbootstrap.com/](https://primevue.org/icons/)) - 超棒的前端图标 库 (A hyper-awesome front-end icon library)

该自定义节点的Python后端会进入模型文件所在的目录，然后寻找与模型名字的相似度最高的markdown文件（相似度算法为Bigram）。若相似度过低，则会打开全空的新Markdown文件，并在用户点击保存后存入模型文件所在目录。

The Python backend of this custom node will search for the markdown file with the highest similarity to the model name (using Bigram similarity algorithm). If the similarity is too low, a new empty markdown file will be opened for the user to edit. The edited content will be saved to the model file directory when the user clicks the "Save" button.

## 开发配置步骤 - Development Configuration Steps

若想尝试修改该自定义节点，或以该自定义节点为基础做二次开发，请按如下步骤配置开发环境。强烈推荐使用fnm来管理node.js版本，真的很好使！

To modify this custom node, please consider following the steps below (fnm is recommended to manage multiple versions of node.js):

1. 将本仓库克隆到ComfyUI的自定义节点目录中（一般位于 `ComfyUI/custom_nodes` ）(Clone this repo into the `custom_nodes` directory of your ComfyUI installation)：
   ```bash
   git clone https://codeberg.org/endericedragon/comfyui-mdnotes.git
   ```
2. 导航到仓库根目录 (Navigate to the root directory of the repository)：
   ```bash
   cd comfyui-mdnotes
   ```
3. 安装依赖NPM包 (Install dependencies using NPM)：
   ```bash
    npm install
   ```
4. 构建项目，vite会把构建产物放到 `web` 目录中 (Build the project using Vite, which will put the build artifacts into the `web` directory)：
   ```bash
   npm run build
   ```
5. 启动 / 刷新ComfyUI网页端界面，即可载入更改 (Start / refresh the ComfyUI web interface to load the changes)。

## 开发日志 - Development Log

ComfyUI关于自定义节点开发的文档质量一言难尽，官方文档内容不全，网络上的教程质量亦参差不齐，故将笔者开发该节点的过程分享于此，有需自取即可，欢迎指正与PR。

### 准备模板

笔者选择使用Vue来开发前端，因此借用了自定义节点的Vue模板。该模板可通过如下命令获得：

```bash
comfy node scaffold
```

在回答一系列问题后即可获得模板（注意在它询问使用什么模板时选择Yes, use Vue...那一项）。

接下来使用VS Code打开模板。此时Code会给.py文件里的大量内容标红线表示找不到，此时做两件事情：

1. 将解释器设置成ComfyUI所使用的那个Python解释器。
2. 在 `.vscode/settings.json` 中，设置 `"python.analysis.extraPaths"`和 `"python.autoComplete.extraPaths"`为ComfyUI的根目录，即 `server.py`, `nodes.py`等文件所在的那个目录

此时.py文件中的红线会消失大半，.ts, .vue文件中的红线可能还有，这个就得碰运气了，有时候Code连 `import {...} from 'vue'`也会标红线，此时建议：要么重新运行 `npm i`，要么按Ctrl+Shift+P打开面板，然后选择“重启Vue语言服务器”，有可能就好了。计算机，很神奇吧~

至于前端文件中把 `../../../scripts/app.js` 等内容标红，目前尚无解决办法。

> 观察 `package.json` 会发现，其中的依赖项有 `dependencies` 和 `peerDependendies` 两项。它们的区别在于：NPM假设宿主机已经安装了 `peerDependencies` ，故不会主动安装这些包。在ComfyUI自定义节点的开发环境中，诸如 `vue-i18n, vue, primevue` 等组件已经由ComfyUI提供，故无需额外安装，且在 `vite.config.mts` 中还需要将它们列为 `externel` 。

### 编写前端

编写前端的办法基本上和普通的Vue项目没差，但最终装载 Vue 组件的TS代码有差异，本仓库的这部分代码有如下注意点：

```typescript
// -- snip --

// 这行是一定会被标红的，没办法
import { app } from "../../../scripts/app.js";
// 用它给 app.js 标注类型的话，可以利用自动补全写代码，很爽
import type { ComfyApp } from '@comfyorg/comfyui-frontend-types'
const comfyApp: ComfyApp = app;

// 想要加载CSS吗？那就引入它吧
import * as utils from '../../../scripts/utils.js';
// extensions是固定的
// comfyui-mdnotes是自定义节点的目录名字
// 后续内容和/js目录有关，而js目录结构取决于vite.config.mts
// 具体来说是取决于build.rollupOptions.output以及build.outDir
// 建议把build.rollupOptions.output.dir和build.outDir设置成一样的
utils.addStylesheet("extensions/comfyui-mdnotes/assets/main.css");

// -- snip --
comfyApp.registerExtension({
  name: "endericedragon.mdnotes",
  // 装载一定要在页面元素都齐活之后再做
  async setup() {
    // 使用TS生成挂载点
    let mountPoint = document.createElement("div");
    mountPoint.id = "mdnotes-ui";
    document.body.appendChild(mountPoint);
    // 然后把Vue组件挂载到挂载点上即可
    createApp(App).mount(mountPoint);
  }
});
```

> 这儿有两个点需要注意：
>
> 1. 添加CSS的方法，就是 `utils.addStylesheet` 函数；其用法和参数在注释里写得很清楚了。
> 2. （不稳定，存疑）添加其他自定义文件的办法，例如 `.json` 文件，放在项目根目录的 `public` 目录中，这样Vite在编译时就会把他们原封不动地复制到 `web` 目录下。再用 `utils.uploadFile` 即可上传该文件供其他代码使用。

> 更新 [2025.12.12]
> 
> 现在引用app和utils的方法有所变化，不再会划红线了，具体而言，现在如此引用两者：
> ```typescript
> const app = window.comfyAPI.app.app;
> const utils = window.comfyAPI.utils;
> ```

注册右键菜单的方法如下：

```typescript
comfyApp.registerExtension({
    name: "endericedragon.mdnotes",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        let originalMenuOptions = nodeType.prototype.getExtraMenuOptions;
        nodeType.prototype.getExtraMenuOptions = function (_, options) {
            // 调用原始方法
            originalMenuOptions?.apply(this, arguments);
            // 新增菜单项
            options.unshift({
                    content: "Show lora note",
                    callback: () => { ... }
            });
        }
    }
});
```

此外，为了实现灵活的信息传递，本项目大量使用事件监听器实现跨组件通信，如下：

```typescript
window.addEventListener("event-id", e => {
  let detail = (e as CustomEvent).detail;
  // detail的结构与发送事件时保持一致
  detail["content"]...
  detail["filename"]...
})

window.dispatchEvent(
  new CustomEvent("event-id", { 
    detail: { 
      content: "hello", filename: "test.md" 
    } 
  })
)
```

### 编写后端

本仓库的后端全部写在 `__init__.py` 中，具体编写方法较为简单，自行查阅即可。此处仅介绍一下前后端通信（确切地说是前发后收）的写法。

从前端发送消息到后端比较简单。本仓库已经将这个过程封装到 `constants.ts` 的 `postJsonData` 函数中，观察其实现不难发现，就是对ComfyUI的 `app.api.fetchApi` 函数的封装：

```ts
import type { ComfyApp } from '@comfyorg/comfyui-frontend-types'

async function postJsonData(app: ComfyApp, route: string, data: any) {
    return app.api.fetchApi(route, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    }).then(res => res.json());
}
```

后端通过给 `server.PromptServer` 配置路由来接收前端的消息：

```py
# 此处的路径 /path/to/sth 需要和调用 postJsonData 时的 route 匹配
@PromptServer.instance.routes.post("/path/to/sth")
async def do_sth(request: web.Request):
    data: dict[str, str] = await request.json()
    # -- snip --
    return web.json_response({"status": "ok"}, status=200)
```
