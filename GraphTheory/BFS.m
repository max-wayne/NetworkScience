function node_visit=BFS(A, start_node)
% A: graph, start_node: node be searched at first.
% node_visit: result of searching.
node_visit=start_node; 
queue=start_node;
while ~isempty(queue)
    neib=find(A(queue(1),:)==1);
    for j=1:length(neib)
        if ~ismember(neib(j),node_visit)
            node_visit=[node_visit neib(j)];
            queue=[queue neib(j)];
        end
    end
    queue(1)=[];
end
