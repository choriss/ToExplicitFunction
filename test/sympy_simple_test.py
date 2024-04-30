import sympy 
import latex2sympy2

eq1 = sympy.simplify(latex2sympy2.latex2sympy(r"\sqrt{\left(x-n\right)^{2}+y^{2}}+\sqrt{\left(x-m\cos\left(\theta{1}\right)\right)^{2}+\left(y-m\sin\left(\theta{1}\right)\right)^{2}}+\sqrt{\left(x-l\cos\left(\theta{2}\right)\right)^{2}+\left(y+l\sin\left(\theta{2}\right)\right)^{2}}-a+n-\sqrt{\left(m\cos\left(\theta{1}\right)-a\right)^{2}+m^{2}\sin^{2}\left(\theta{1}\right)}-\sqrt{\left(l\cos\left(\theta{2}\right)-a\right)^{2}+l^{2}\sin^{2}\left(\theta{2}\right)}"))

print(eq1)

print(sympy.solve(eq1,"y"))