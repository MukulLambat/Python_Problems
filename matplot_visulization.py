#%%
import matplotlib.pyplot as plt
import seaborn as sns
import pl
#%%
epochs = [1, 2, 3, 4, 5]
training_loss = [0.9, 0.6, 0.5, 0.4, 0.35]
val_loss = [1.0, 0.7, 0.6, 0.5, 0.45]
#%%
plt.plot(epochs, training_loss, label = 'Training Loss')
plt.plot(epochs, val_loss,label = 'Validation Loss')
plt.title("Loss vs Epochs")
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
# %%
classes = ['Setosa', 'versicolor', 'virginica']
counts = [30, 40, 50]
plt.bar(classes, counts)
plt.title('Bar Plot')
plt.xlabel('Classes')
plt.ylabel('Counts')
plt.show()
# %%
df = sns.load_dataset('titanic')
sns.countplot(x = 'survived', data=df)
plt.xlabel("Survived 0 = No 1 = Yes")
# %%
