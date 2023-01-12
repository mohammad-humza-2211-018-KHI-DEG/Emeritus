from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def get_data():
    """Return a tuple containing:
    * training features
    * test features
    * training targets
    * test targets
    * data preprocessing function (already applied to the provided data)
    When serving the model in production you might need to preprocess the raw input data. You can
    use the last element of the returned tuple for this.
    """
    wine = datasets.load_wine()
    wine_x = wine.data
    wine_y = wine.target

    x_train, x_test, y_train, y_test = train_test_split(
        wine_x, wine_y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    return (x_train, x_test, y_train, y_test, lambda x: scaler.transform(x))
