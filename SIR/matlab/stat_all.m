function stat_all(p)
%% load data.
load(strcat(p, 'see_dict')); load(strcat(p, 'ret_dict')); load(strcat(p, 'ret_num'));
%% calculate.
% t1: 接收到信息的人接收次数；t2: 转发信息的人转发前接收到的次数；t3: 转发的人转发的次数
t1 = tabulate(see_dict(:, 2)); t2 = tabulate(ret_dict(:, 2)); t3 = tabulate(ret_num(:, 2));
% ret_x1: 正好接收到==x次的人中，有多少人在前x次转发
% ret_x2: 正好接收到>=x次的人中，有多少人在前x次转发
% ret_x3: 正好接收到==x次的人中，有多少人在第x次转发
% beta_x1: 正好接收到==x次并且前x-1次没有转发的人中，有多少人在第x次转发
% beta_x2: 正好接收到>=x次并且前x-1次没有转发的人中，有多少人在第x次转发
ret_x1 = []; ret_x2 = []; ret_x3 = []; beta_x1 = []; beta_x2 = [];
for i = 1 : 200
    u1 = see_dict(see_dict(:, 2)==i, 1); u2 = see_dict(see_dict(:, 2)>=i, 1);
    u3 = ret_dict(ret_dict(:, 2)==i, 1); u4 = ret_dict(ret_dict(:, 2)<=i, 1);
    ret_x1 = [ret_x1 length(intersect(u1, u4))/length(u1)];
    ret_x2 = [ret_x2 length(intersect(u2, u4))/length(u2)];
    ret_x3 = [ret_x3 length(intersect(u2, u3))/length(u2)];
    u5 = ret_dict(ret_dict(:, 2)<i, 1); u6 = setdiff(u1, u5);
    beta_x1 = [beta_x1 length(intersect(u3, u6))/length(u6)];
    u7 = setdiff(u2, u5);
    beta_x2 = [beta_x2 length(intersect(u3, u7))/length(u7)];
end
%% save results.
save(strcat(p, 'res.mat'), 't1', 't2', 't3', 'ret_x1', 'ret_x2', 'ret_x3', 'beta_x1', 'beta_x2');
