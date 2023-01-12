import data
import model
from sklearn.metrics import f1_score
from sklearn.preprocessing import StandardScaler


def main():
    x_train, x_test, y_train, y_test, _ = data.get_data()
    knn_model = model.get_model(x_train, y_train)
    y_pred = knn_model.predict(x_test)
    print(f1_score(y_test, y_pred, average="micro"))


if __name__ == "__main__":
    main()
