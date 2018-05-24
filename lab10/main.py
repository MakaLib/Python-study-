import draw
import calka

wsp1 = ((0,0,0,0,0.16,0), (0.2,-0.26,0,0.23,0.22,1.6), (-0.15,0.28,0,0.26,0.24,0.44), (0.85,0.04,0,-0.04,0.85,1.6))

draw.przeksztalc(wsp1)
print(calka.MonteCarlo(lambda x: x*x + 2*x, 0 ,20))
print(calka.pi(1000))
draw.drugie()