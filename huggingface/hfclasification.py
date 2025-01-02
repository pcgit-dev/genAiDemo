from datasets import load_dataset
from transformers import AutoTokenizer
from transformers import TrainingArguments
from transformers import Trainer
from transformers import AutoModelForSequenceClassification



#Load Data
dataset = load_dataset("imdb")

#Select tokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")

#Tokenize the dataset
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

#Load pretrained model
model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased", num_labels=2)

tokenized_datasets = dataset.map(tokenize_function, batched=True)
training_args=TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["test"],

)

trainer.train()
result = trainer.evaluate()
print(result)

model.save_pretrained("./results")
tokenizer.save_pretrained("./results")