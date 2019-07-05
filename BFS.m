clear; clc;
load('./A');
% n=100;d=1.5;
% A=Create_ER_dir_network(n,d);
% h=view(biograph(A));
% dist=graphallshortestpaths(A, 'DIRECTED', true);

node_visit=1; queue=1; % 从第一个节点开始搜索
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



