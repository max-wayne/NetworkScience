function [gs,g]=giant_component(A)
%gs: the size of giant component
%g: the node in giant component
[S,C]=graphconncomp(A);
c=0;
for i=1:S
    idx=find(C==i);
    if length(idx)>c
        c=length(idx);
        g=idx;
    end
end
gs=length(g)/length(A(:,1));

