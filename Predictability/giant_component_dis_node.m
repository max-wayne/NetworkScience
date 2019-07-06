function node_g=giant_component_dis_node(A)
%A: the network
%node_g: the size of component of node i belong to
n=length(A(:,1));
[~,C]=graphconncomp(A);
node_g(n)=0;
for i=1:n
    a=find(C==C(i));
    node_g(i)=length(a);
end
