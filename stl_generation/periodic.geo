nd = 0.380937;
nv = 3.39152;
lx = 63.05*nd;

distAmp = 0.20;

gridsize = nd/32;

piVal = 3.1415926;

extudeLength = lx;

Point(1) = {0, 0, 0, gridsize};
Point(2) = {0, 0, nd, gridsize};
Point(3) = {lx, 0, nd, gridsize};
Point(4) = {lx, 0, 0, gridsize};

Line(1) = {2, 1};
Line(2) = {1, 4};
Line(3) = {4, 3};

pList[0] = 2; // First point label
nPoints = 40; // Number of discretization points (top-right point of the inlet region)
For i In {1 : nPoints}
    x = 0.0 + lx*i/(nPoints + 1);
    pList[i] = newp;
    Point(pList[i]) = {x, 0,
                (nd*(1.0+distAmp*Sin(2.0*piVal*x/lx))),
                gridsize};
EndFor
pList[nPoints+1] = 3; // Last point label (top-left point of the outlet region)

Spline(newl) = pList[];

Transfinite Line {1, -3} = Ceil(nd/gridsize)  Using Progression 1;
Transfinite Line {2, 4} = Ceil(lx/gridsize)  Using Progression 1;

Line Loop(110) = {1, 2, 3, -4};
Plane Surface(120) = {110};

Transfinite Surface {120};
Recombine Surface {120};

Extrude {0, extudeLength, 0} {
    Surface{120}; Layers{1}; Recombine;
}
Coherence;//+
Physical Surface(143) = {129};
//+
Physical Surface("leftBound", 144) = {129};
//+
Physical Surface("rightBound", 145) = {137};
//+
Physical Surface("frontBack", 146) = {142, 120};
//+
Physical Surface("topBottom", 147) = {141, 133};
//+
Physical Volume("internal", 148) = {1};
