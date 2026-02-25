Creates lora from two checkpoints by extracting the difference.

model_a is the base model

model_b is the finetuned model

rank is the final rank of the model, higher = larger size

method is rsvd (fast, but marginally less precise) or svd

There are two ways to extract, rsvd which is faster and 99% as good as svd, you can choose oversampling for this one.
