import tensorflow as tf
import tensorflow_datasets as tfds
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer

# Load the dataset
data, info = tfds.load('wikipedia/20190301.en', with_info=True)

# Instantiate the tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = TFGPT2LMHeadModel.from_pretrained('gpt2')

# Tokenize the dataset
def encode(texts):
    return tokenizer.batch_encode_plus(texts, pad_to_max_length=True, return_tensors='tf')

dataset = data['train'].batch(16).map(lambda x: encode(x['text']))

# Define the training parameters
optimizer = tf.keras.optimizers.Adam(learning_rate=3e-5, epsilon=1e-08, clipnorm=1.0)
loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
metric = tf.keras.metrics.SparseCategoricalAccuracy('accuracy')
model.compile(optimizer=optimizer, loss=[loss, *[None] * model.config.n_layer], metrics=[metric])

# Train the model
model.fit(dataset, epochs=5, steps_per_epoch=200)

# Save the model
model.save_pretrained('models/chatbot')
