import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn import metrics, svm
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from market_place import MarketPlace
from repository import save_in_csv
from utils import constansts

"""
Here we predict the num of active installs based on average price
with three algorithms random forest, SVM(linear) and linear regression
and at the end, we compare their results
"""

result_sdf = pd.DataFrame()


def get_data() -> pd.DataFrame:
    """
    :return the data frame that we want process on it
    """
    m = MarketPlace()
    df = m.df[["active_installs"]].copy()

    df["price"] = m.retrieve_avg_price().copy()
    return df[(df['price'] >= 0) & (df['active_installs'] >= 0)]


def evaluation_matrix(y_true, y_predict):
    """
    For evaluation of error term
    """
    print('Mean Squared Error: ' + str(metrics.mean_squared_error(y_true, y_predict)))
    print('Mean absolute Error: ' + str(metrics.mean_absolute_error(y_true, y_predict)))


def evaluation_matrix_dict(y_true, y_predict, name='Linear'):
    """
    To add into results_index for evaluation of error term
    """
    dict_matrix = {
        'Series Name': name,
        'Mean Squared Error': metrics.mean_squared_error(y_true, y_predict),
        'Mean Absolute Error': metrics.mean_absolute_error(y_true, y_predict)
        # 'Mean Squared Log Error': metrics.mean_squared_log_error(y_true, y_predict)
    }
    return dict_matrix


def linear_regression_learn():
    """
    Learn data and predict installs base price via linear regression
    """
    df = get_data()
    # Integer encoding
    x = df.drop(labels=['price'], axis=1)
    y = df['active_installs']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30)
    model = LinearRegression()
    model.fit(x_train, y_train)
    results = model.predict(x_test)

    # Creation of results data frame and addition of first entry
    global result_sdf
    result_sdf = result_sdf.append(evaluation_matrix_dict(y_test, results, name='Linear_regression'),
                                   ignore_index=True)
    print("-------------------------------------------------")
    print("linear regression results:")
    print('Actual mean of installs:' + str(y.mean()))
    print('Predicted installs(mean) :' + str(results.mean()))
    print('Predicted installs(std) :' + str(results.std()))
    print("-------------------------------------------------")

    plt.figure(figsize=(12, 7))
    sns.regplot(x=results, y=y_test, color='teal', label='Price', marker='x')
    plt.legend()
    plt.title('linear regression learn # installs from avg price')
    plt.xlabel('Predicted installs')
    plt.ylabel('Actual installs')
    plt.show()


def random_forest_learn():
    """
    Learn data and predict installs base price via random forest algorithm
    and plot its result
    """

    df = get_data()
    x = df.drop(labels=['price'], axis=1)
    y = df['active_installs']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30)

    model = RandomForestRegressor()
    model.fit(x_train, y_train)
    results = model.predict(x_test)

    # evaluation
    global result_sdf
    result_sdf = result_sdf.append(evaluation_matrix_dict(y_test, results, name='Random forest'),
                                   ignore_index=True)
    print("-------------------------------------------------")
    print("random forest results:")
    print('Actual mean of installs:' + str(y.mean()))
    print('Predicted installs(mean) :' + str(results.mean()))
    print('Predicted installs(std) :' + str(results.std()))
    print("-------------------------------------------------")

    plt.figure(figsize=(12, 7))
    sns.regplot(x=results, y=y_test, color='teal', label='Price', marker='x')
    plt.legend()
    plt.title('Random forest learn # installs from avg price')
    plt.xlabel('Predicted installs')
    plt.ylabel('Actual installs')
    plt.show()


def svm_learn():
    # Integer encoding
    df = get_data()
    x = df.drop(labels=['price'], axis=1)
    y = df['active_installs']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30)

    model = svm.LinearSVR()
    model.fit(x_train, y_train)

    results = model.predict(x_test)

    global result_sdf
    result_sdf = result_sdf.append(evaluation_matrix_dict(y_test, results, name='SVM-linear'),
                                   ignore_index=True)

    print('Actual mean of installs:' + str(y.mean()))
    print('Predicted installs(mean) :' + str(results.mean()))
    print('Predicted installs(std) :' + str(results.std()))

    plt.figure(figsize=(12, 7))
    sns.regplot(x=results, y=y_test, color='teal', label='Price', marker='x')
    plt.legend()
    plt.title('SVM learn # installs from avg price')
    plt.xlabel('Predicted installs')
    plt.ylabel('Actual installs')
    plt.show()


def compare_learners():
    """
    Compare two algorithms linear regression and random forest results and show it
    and plot its result
    """

    global result_sdf
    linear_regression_learn()
    svm_learn()
    random_forest_learn()

    # print errors together
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(result_sdf)

    # save errors to a csv file
    save_in_csv("log/errors.csv", result_sdf)

    # plot errors to compare them
    result_sdf.set_index('Series Name', inplace=True)

    plt.subplot(2, 1, 1)
    result_sdf['Mean Squared Error'].sort_values(ascending=False).plot(kind='barh', color=constansts.green,
                                                                       title='Mean Squared Error')
    plt.subplot(2, 1, 2)
    result_sdf['Mean Absolute Error'].sort_values(ascending=False).plot(kind='barh', color=constansts.orange,
                                                                        title='Mean Absolute Error')
    plt.show()


if __name__ == "__main__":
    compare_learners()
