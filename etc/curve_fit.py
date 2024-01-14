#include <iostream>
#include <vector>
#include <cmath>

struct DataPoint {
    double x;
    double y;
};

std::vector<double> fitCurve(const std::vector<DataPoint>& data) {
    double x_sum = 0, y_sum = 0, x2_sum = 0, x3_sum = 0, x4_sum = 0, xy_sum = 0, x2y_sum = 0;
    int n = data.size();

    for(const auto& point : data) {
        double x = point.x;
        double y = point.y;
        double x2 = x * x;
        double x3 = x2 * x;
        double x4 = x2 * x2;

        x_sum += x;
        y_sum += y;
        x2_sum += x2;
        x3_sum += x3;
        x4_sum += x4;
        xy_sum += x * y;
        x2y_sum += x2 * y;
    }

    std::vector<std::vector<double>> A = {{x4_sum, x3_sum, x2_sum}, {x3_sum, x2_sum, x_sum}, {x2_sum, x_sum, n}};
    std::vector<double> B = {x2y_sum, xy_sum, y_sum};

    // Gaussian elimination
    for(int i = 0; i < 3; i++) {
        for(int j = i + 1; j < 3; j++) {
            double ratio = A[j][i] / A[i][i];
            for(int k = 0; k < 3; k++) {
                A[j][k] -= ratio * A[i][k];
            }
            B[j] -= ratio * B[i];
        }
    }

    std::vector<double> coeffs(3);
    for(int i = 2; i >= 0; i--) {
        for(int j = i + 1; j < 3; j++) {
            B[i] -= A[i][j] * coeffs[j];
        }
        coeffs[i] = B[i] / A[i][i];
    }

    return coeffs;
}

int main() {
    std::vector<DataPoint> data = {{0, 1}, {1, 4}, {2, 9}, {3, 16}, {4, 25}}; // 예제 데이터

    std::vector<double> coeffs = fitCurve(data);

    std::cout << "계수: ";
    for(double coeff : coeffs) {
        std::cout << coeff << ' ';
    }
    std::cout << std::endl;

    return 0;
}
