#include <iostream>
#include<tuple>
#include <math.h>

using namespace std;

class point {

    public:
        point(double x, double y) {
            this->x = x;
            this->y = y;
        }

        double x;
        double y;
};

void afinize(tuple<double, double, double>& T4) {
    
    cout << "T4(" << round(get<0>(T4) /get<2>(T4)) << ", " << round(get<1>(T4) / get<2>(T4)) <<  ")" << endl;
}

tuple<double, double, double> cross_product(tuple<double, double, double> p1, tuple<double, double, double> p2) {

    double x = get<1>(p1) * get<2>(p2) - get<2>(p1) * get<1>(p2);
    double y = get<2>(p1) * get<0>(p2) - get<0>(p1) * get<2>(p2);
    double z = get<0>(p1) * get<1>(p2) - get<0>(p2) * get<1>(p1);

    return make_tuple(x, y, z);
}

tuple<double, double, double> invisible(point& T1, point& T2, point& T3, point& T5, point& T6, point& T7, point& T8) {

    tuple<double, double, double> t1 = make_tuple(T1.x, T1.y, 1), 
                                  t2 = make_tuple(T2.x, T2.y, 1), 
                                  t3 = make_tuple(T3.x, T3.y, 1), 
                                  t5 = make_tuple(T5.x, T5.y, 1),
                                  t6 = make_tuple(T6.x, T6.y, 1),
                                  t7 = make_tuple(T7.x, T7.y, 1),
                                  t8 = make_tuple(T8.x, T8.y, 1);

    tuple<double, double, double> x_infinity = cross_product(cross_product(t1, t5), cross_product(t2, t6));
    /*tuple<double, double, double> x_infinity_2 = cross_product(cross_product(t1, t5), cross_product(t3, t7));
    tuple<double, double, double> x_infinity_3 = cross_product(cross_product(t2, t6), cross_product(t3, t7));*/

    tuple<double, double, double> y_infinity = cross_product(cross_product(t5, t6), cross_product(t8, t7));
    /*tuple<double, double, double> y_infinity_2 = cross_product(cross_product(t5, t6), cross_product(t1, t2));
    tuple<double, double, double> y_infinity_3 = cross_product(cross_product(t1, t2), cross_product(t7, t8));*/

    return cross_product(cross_product(x_infinity, t8), cross_product(y_infinity, t3));
}

int main() {
/*
    //piksel koordinate tacaka sa slike
    point T1(162, 404);
    point T2(678, 765);
    point T3(894, 466);
    point T5(92, 198);
    point T6(705, 520);
    point T7(958, 248);
    point T8(392, 88);
  
    point T1(418, 295);
    point T2(733, 484);
    point T3(985, 319);
    point T5(378, 201);
    point T6(724, 360);
    point T7(1010, 220);
    point T8(644, 145);
  */
    point T1(515, 330);
    point T2(661, 461);
    point T3(887, 245);
    point T5(471, 188);
    point T6(644, 311);
    point T7(905, 108);
    point T8(740, 59);
    
    //piksel koordinate nevidljive tacke
    tuple<double, double, double> T4 = invisible(T1, T2, T3, T5, T6, T7, T8);

    afinize(T4);

    return 0; 
}
