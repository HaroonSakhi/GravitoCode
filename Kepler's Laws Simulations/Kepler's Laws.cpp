/*
 Author: Haroon Sakhi
 Description: This code was developed by Haroon Sakhi as part
 of the project Kepler's Laws Simulations.
 Any use or modification of this code should include proper
 attribution to the original author.
*/

#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

double G = 6.6743e-11;
double M = 1.989e30;
double Au = 1.496e+11;
double dt = 30;

class Planet
{
public:
    double mass;
    double vel[2];
    double pos[2];
    double acc[2];
};

double Force(double r, double mass)
{
    double F = (G * M * mass) * (1 / pow(r, 2));
    return -F;
}

double Radius(double x, double y)
{
    double R = sqrt((x * x) + (y * y));
    return R;
}

double Area(double r, double theta)
{
    double a = 0.500 * (r * r) * theta;
    return a;
}

int main()
{
    ofstream earth("earth.txt");
    ofstream mars("mars.txt");

    Planet planets[2];

    planets[0].mass = 5.97219e24;
    planets[0].vel[0] = 0;
    planets[0].vel[1] = 30e3;
    planets[0].pos[0] = Au;
    planets[0].pos[1] = 0;

    planets[1].mass = 6.39e23;
    planets[1].vel[0] = 0;
    planets[1].vel[1] = 24e3;
    planets[1].pos[0] = 1.500 * Au;
    planets[1].pos[1] = 0;

    Planet Mars = planets[1];
    Planet Earth = planets[0];

    double time = 31536000;
    double a, theta0, theta, r, ax, ay;
    double am, rm, axm, aym;
    double area = 0;
    theta0 = 0;
    theta = 0;
    area = 0;

    for (int t = 0; t < time; t = t + dt)
    {
        theta0 = atan((Earth.pos[1]) / (Earth.pos[0]));

        earth << t << " " << Earth.pos[0] << " " << Earth.pos[1] << " " << area << endl;
        mars << t << " " << Mars.pos[0] << " " << Mars.pos[1] << " " << area << endl;

        r = Radius(Earth.pos[0], Earth.pos[1]);
        rm = Radius(Mars.pos[0], Mars.pos[1]);
        a = Force(r, Earth.mass) / Earth.mass;
        am = Force(rm, Mars.mass) / Mars.mass;

        ax = a * (Earth.pos[0] / r);
        ay = a * (Earth.pos[1] / r);
        axm = am * (Mars.pos[0] / r);
        aym = am * (Mars.pos[1] / r);

        Earth.vel[0] += ax * dt;
        Earth.vel[1] += ay * dt;
        Mars.vel[0] += axm * dt;
        Mars.vel[1] += aym * dt;

        Earth.pos[0] += (Earth.vel[0] * dt) + 0.500 * (ax * pow(dt, 2));
        Earth.pos[1] += (Earth.vel[1] * dt) + 0.500 * (ay * pow(dt, 2));

        Mars.pos[0] += (Mars.vel[0] * dt) + 0.500 * (axm * pow(dt, 2));
        Mars.pos[1] += (Mars.vel[1] * dt) + 0.500 * (aym * pow(dt, 2));

        theta = atan((Earth.pos[1]) / (Earth.pos[0]));
        theta = theta - theta0;
        area = Area(r, theta);
    }

    return 0;
}
