function plot_para_vs_paraX()
clear; clc;
load('D:\double_check\info\stat_results\beta1_a_b_2017_trunc10');
beta1 = para(:, 1); a = para(:, 2); b = para(:, 3);
%% ko与beta1,a,b的关系
d = load('D:\double_check\info\stat_results\repost_info_ki.txt');
ko = d(370:end);
% plot ko V.S. beta1
figure(); loglog(ko, beta1, 'o');
% plot ko V.S. a
figure(); idx = a ~= 1; semilogx(ko(idx), a(idx), 'o');
% plot ko V.S. b
figure(); semilogx(ko(idx), b(idx), 'o');

%% RepostTime与beta1,a,b的关系
d = load('D:\double_check\info\stat_results\repost_info_time.txt');
t = d(370:end);
% plot RepostTime dist.
figure(); [m, n] = hist(t, 24); bar(n, m/length(t));
% plot RepostTime V.S. beta1
idx = find(beta1<=3e-3);
figure(); plot(t(idx), beta1(idx), 'p'); hold on;
time_beta1 = [];
for i = 0 : 23
    if length(find(t==i)) >= 1
        time_beta1 = [time_beta1; [i, mean(beta1(t==i))]];
    end
end
plot(time_beta1(:, 1), time_beta1(:, 2), 'r--o');                 
% plot RepostTime V.S. a
idx = find(a~=1); a = a(idx); b = b(idx); t = t(idx);
figure(); plot(t, a, 'p'); hold on;
time_a = [];
for i = 0 : 23
    if length(find(t==i)) >= 1
        time_a = [time_a; [i, mean(a(t==i))]];
    end
end
plot(time_a(:, 1), time_a(:, 2), 'r--o');
% plot RepostTime V.S. b
figure(); plot(t, b, 'p'); hold on;
time_b = [];
for i = 0 : 23
    if length(find(t==i)) >= 1
        time_b = [time_b; [i, mean(b(t==i))]];
    end
end
plot(time_b(:, 1), time_b(:, 2), 'g--o');
%% SurvivalTime与beta1,b,c的关系
load('D:\double_check\info\stat_results\SurvivalTime');
% plot T dist.
figure(); idx_t = find(T<200);
[m, n] = hist(T(idx_t), 20); bar(n, m./length(T(idx_t)));
% plot T V.S. beta1
figure(); semilogy(T(idx_t), beta1(idx_t)', 'o')
% plot T V.S. a
a = para(:, 2);
figure(); plot(T(intersect(idx, idx_t)), a(intersect(idx, idx_t)), 'ro')
% plot T V.S. b
b = para(:, 3);
figure();  plot(T(intersect(idx, idx_t)), b(intersect(idx, idx_t)), 'ro')

