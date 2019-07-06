function [gs,g,B]=bond_percolation(A,p)
% A: network, p: probabilty of occupied an edge.
% B: network after bond percolation, gs: gaint component, g: node in gs
N=length(A(:,1));
B=tril(A);
c=find(B==1); n=length(c);
y=randperm(n);
fa=y(1:ceil(n*(1-p))); % ÒªÉ¾³ýµÄ±ß
c(fa)=[];
B=sparse(N,N);
B(c)=1;
B=B+B';
[gs,g]=giant_component2(B);
