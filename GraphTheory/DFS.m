function node_visit=DFS(A, start_node)
% A: graph, start_node: node be searched at first.
% node_visit: result of searching.
node_visit=start_node;
stack=start_node; top=1;
while ~isempty(stack)
    len1=length(stack);
    neib=find(A(stack(top),:)==1);
    for i=1:length(neib)
        if ~ismember(neib(i), node_visit)
            top=top+1;
            node_visit=[node_visit neib(i)];
            stack(top)=neib(i);
            break;
        end
    end
    if length(stack)==len1
        stack(top)=[];
        top=top-1;
    end
end


