/* Scaler.c : program for scaling data files with x,y pairs of values.
** Upinder S. Bhalla, Caltech, June 1992.
*/

#include <stdio.h>
#include <math.h>

#define XSCALE 1.0
#define YSCALE 1.0
#define XOFFSET 0.0
#define YOFFSET 0.0

int main(argc,argv)
	int argc;
	char	**argv;
{
	int i;
	float	x,y;
	double	atof();
	FILE	*fp,*fopen(),*fout;
	float	sx=XSCALE,sy=YSCALE,ox=XOFFSET,oy=YOFFSET;
	int		ret;

	if (argc < 7) {
		printf("usage: %s infile outfile sx sy ox oy\n",
			argv[0]);
                return -1;
	}
	i=3;
	sx=atof(argv[i]);
	i++; sy=atof(argv[i]);
	i++; ox=atof(argv[i]);
	i++; oy=atof(argv[i]);
	

	fp=fopen(argv[1],"r");
	fout=fopen(argv[2],"w");

	for (i=0;  ;i++) 
        {
                ret=fscanf(fp,"%f%f",&x,&y);
		if(EOF == ret) break;
		if (0 == ret) continue;
		x -= ox;
		y -= oy;
		x *= sx;
		y *= sy;
		fprintf(fout,"%f	%f\n",x,y);
	}
	fclose(fp);
	fclose(fout);
        return 0;
}
