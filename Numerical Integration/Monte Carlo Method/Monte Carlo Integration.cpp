/*
* Author: Haroon Sakhi
* Description: This code was developed by Haroon Sakhi as part
* of the project Numerical Integration.
* Any use or modification of this code should include proper
* attribution to the original author.
*/

#include <iostream>
#include <math.h>
#include <time.h>

using namespace std;

//The function we want to integrate
float func(float x)
{
    return exp(-2 * x);
}

int main()
{
    srand(time(NULL));//Makes sure answer is different each time
    
    //Initializing values
    int totalPoints = 10000000.0;
    int pointUnderCurve = 0.0;

    float length = 2.5;
    float height = 1.3;

    float area = length * height;

    float x = 0;
    float y = 0;


    for(int i = 0; i < totalPoints; i++)
    {
        float xRand = (float)rand() / RAND_MAX;//These are temporary variables that are between 0 and 1
        float yRand = (float)rand() / RAND_MAX;

        x = xRand * length;//Using the temporary variables we scale them to fit in the rectangle
        y = yRand * height;

        if (y < func(x))
        {
            pointUnderCurve++;
        }
    }

    float areaUnderCurve = ((double) pointUnderCurve / (double) totalPoints) * area;
    cout << "Area under curve: " << areaUnderCurve;
}