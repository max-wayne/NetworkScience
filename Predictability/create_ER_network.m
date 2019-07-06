function A=create_ER_network(n,d)
% n: the network size, d: average degree
d=d/2; A=sparse(n,n); t=1;
while t<=n*d
    i=randi(n); j=randi(n);
    if i~=j
        A(i,j)=1;
        A(j,i)=1;
        t=t+1;
    end
end

