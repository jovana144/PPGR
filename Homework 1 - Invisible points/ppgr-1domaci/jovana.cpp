#include <iostream>
#include <tuple>
#include <utility>
#include <math.h>

using namespace std;

/*Afine koordinate (5, 3, 4)->(5/4, 3/4, 1)->(5/4, 3/4)*/
void afine(tuple<double, double, double>& tacka4)
{
   cout << "T4(" << round(get<0>(tacka4) / get<2>(tacka4)) << ", " << round(get<1>(tacka4) / get<2>(tacka4))  << ")" << endl;
}

/*vektorski proizvod racunat preko koordinata tacaka*/
tuple<double, double, double> vektorski_proizvod(tuple<double, double, double> p1, tuple<double, double, double> p2)
{
    double x = get<1>(p1) * get<2>(p2) - get<2>(p1) * get<1>(p2);
    double y = get<2>(p1) * get<0>(p2) - get<0>(p1) * get<2>(p2);
    double z = get<0>(p1) * get<1>(p2) - get<0>(p2) * get<1>(p1);

    return make_tuple(x, y, z);
}


tuple<double, double, double> nevidljive(pair<double, double>& T1, pair<double, double>& T2,pair<double, double>& T3,pair<double, double>& T5, pair<double, double>& T6,pair<double, double>& T7,pair<double, double>& T8) {
  
    tuple<double, double, double> t1 = make_tuple(T1.first, T1.second, 1), 
                                  t2 = make_tuple(T2.first, T2.second, 1), 
                                  t3 = make_tuple(T3.first, T3.second, 1), 
                                  t5 = make_tuple(T5.first, T5.second, 1),
                                  t6 = make_tuple(T6.first, T6.second, 1),
                                  t7 = make_tuple(T7.first, T7.second, 1),
                                  t8 = make_tuple(T8.first, T8.second, 1);
  
    tuple<double, double, double> x_infinity = vektorski_proizvod(vektorski_proizvod(t1, t5), vektorski_proizvod(t2, t6));
         
    tuple<double, double, double> y_infinity = vektorski_proizvod(vektorski_proizvod(t5, t6), vektorski_proizvod(t8, t7));


    return vektorski_proizvod(vektorski_proizvod(x_infinity, t8), vektorski_proizvod(y_infinity, t3));
}

int main() {
/*
    //piksel koordinate tacaka sa slike
    pair<double, double>T1 (427, 251);
    pair<double, double>T2 (785, 489);
    pair<double, double>T3 (965, 307);
    pair<double, double>T5 (406, 103);
    pair<double, double>T6 (835, 312);
    pair<double, double>T7 (1027, 161);
    pair<double, double>T8 (657, 50);
  /*
    pair<double, double>T1 (147, 336);
    pair<double, double>T2 (296, 542);
    pair<double, double>T3 (600, 330);
    pair<double, double>T5 (131, 191);
    pair<double, double>T6 (288, 339);
    pair<double, double>T7 (632, 186);
    pair<double, double>T8 (434, 110);
  
  */ 
  /*
    pair<double, double>T1 (418, 295);
    pair<double, double>T2 (733, 484);
    pair<double, double>T3 (985, 319);
    pair<double, double>T5 (378, 201);
    pair<double, double>T6 (724, 360);
    pair<double, double>T7 (1010, 220);
    pair<double, double>T8 (644, 145);
  */
    pair<double, double>T1 (515, 330);
    pair<double, double>T2 (661, 461);
    pair<double, double>T3 (887, 245);
    pair<double, double>T5 (471, 188);
    pair<double, double>T6 (644, 311);
    pair<double, double>T7 (905, 108);
    pair<double, double>T8 (740, 59);
    // 738, 178  
  
    //piksel koordinate nevidljive tacke
    tuple<double, double, double> T4 = nevidljive(T1, T2, T3, T5, T6, T7, T8);

    afine(T4);

    return 0; 
}
