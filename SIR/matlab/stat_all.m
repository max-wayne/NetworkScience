function stat_all(p)
%% load data.
load(strcat(p, 'see_dict')); load(strcat(p, 'ret_dict')); load(strcat(p, 'ret_num'));
%% calculate.
% t1: ���յ���Ϣ���˽��մ�����t2: ת����Ϣ����ת��ǰ���յ��Ĵ�����t3: ת������ת���Ĵ���
t1 = tabulate(see_dict(:, 2)); t2 = tabulate(ret_dict(:, 2)); t3 = tabulate(ret_num(:, 2));
% ret_x1: ���ý��յ�==x�ε����У��ж�������ǰx��ת��
% ret_x2: ���ý��յ�>=x�ε����У��ж�������ǰx��ת��
% ret_x3: ���ý��յ�==x�ε����У��ж������ڵ�x��ת��
% beta_x1: ���ý��յ�==x�β���ǰx-1��û��ת�������У��ж������ڵ�x��ת��
% beta_x2: ���ý��յ�>=x�β���ǰx-1��û��ת�������У��ж������ڵ�x��ת��
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
