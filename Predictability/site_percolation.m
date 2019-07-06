function [gs,g,B]=site_percolation(A,p)
% A: network, p: probabilty of occupied a node.
% B: network after site percolation, gs: gaint component, g: node in gs
B=A;
n=length(A(:,1));
y=randperm(n);
fa=y(1:ceil(n*(1-p)));  % ÒªÉ¾³ýµÄµã 
B(fa,:)=0;B(:,fa)=0;  
[gs,g]=giant_component2(B);
