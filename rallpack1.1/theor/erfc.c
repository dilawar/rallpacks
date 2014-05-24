extern float gammq(float, float);
extern float gammp(float, float);

float erfc_(float );

float erfc_(float x)
{
	float result = x < 0.0 ? 1.0+gammp(0.5,x*x) : gammq(0.5,x*x);
        return result;
}
