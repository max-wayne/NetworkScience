function [a, b] = fit_a_b(x, y)
%% fitting diff(beta_x) = a*exp(-b*x)
%{
myfunc = inline('beta(1)*exp(-beta(2)*x)', 'beta', 'x');
beta0 = [0.1, 0.1]; 
beta = nlinfit(x, y, myfunc, beta0); 
a = beta(1); b = beta(2);
%}
f = polyfit(x, log(y), 1); b = real(f(1)); a = exp(real(f(2)));
