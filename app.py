from flask import Flask, render_template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/')
def index():
    # Generate random data
    np.random.seed(0)
    data = np.random.randn(100, 3)
    df = pd.DataFrame(data, columns=['A', 'B', 'C'])

    # Create a plot
    plt.figure(figsize=(10, 6))
    df.plot(kind='line')
    plt.title('Random Data Plot')
    plt.xlabel('Index')
    plt.ylabel('Values')
    plt.show()
    # Save plot as a PNG file
    plt.savefig('static/plot.png')
    plt.close()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)