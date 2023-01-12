from sklearn.neighbors import KNeighborsClassifier


def get_model(x_train, y_train, n_neighbors=5):
    """Return a kNN model trained on provided data."""
    model = KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(x_train, y_train)
    return model
