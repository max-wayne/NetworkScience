function g=giant_component_dis(A)
%g: the size of each component. 
[S,C]=graphconncomp(A);
g=zeros(1,S);
for i=1:S
    idx=find(C==i);
    g(i)=length(idx);
end

