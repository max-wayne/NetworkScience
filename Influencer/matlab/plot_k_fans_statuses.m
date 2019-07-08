function plot_k_fans_statuses()
s = 'D:/Projects/Pycharm/BIGV/data/bigv/ko_fans_statuses/';
avg_fans_statuses_ko = []; idx1 = [];
for i = 18 : 26
    idx1 = [idx1 2^i];
    s1 = strcat(s, num2str(i));
    data1 = load(s1);
    avg_fans_statuses_ko = [avg_fans_statuses_ko mean(data1)];
end
t = 'D:/Projects/Pycharm/BIGV/data/bigv/ki_fans_statuses/';
avg_fans_statuses_ki = []; idx2 = [];
for i = 0 : 12
    idx2 = [idx2 2^i];
    t1 = strcat(t, num2str(i));
    data2 = load(t1);
    avg_fans_statuses_ki = [avg_fans_statuses_ki mean(data2)];
end

figure;
subplot(2, 1, 1);
h1 = semilogx(idx1, avg_fans_statuses_ko, '--o', 'LineWidth', 1, 'Color', 'r', 'MarkerSize', 10, 'MarkerEdgeColor', 'r', 'MarkerFaceColor', 'r');
xlabel('$K_{o}$', 'interpreter', 'Latex');
ylabel('$fans\_statuses$', 'interpreter', 'Latex');
% legend(h1, 'ko\_statuses\_count', 'location', 'NE');
xlim([520000, 1e8]);
set(gca, 'FontSize', 18);
set(gca, 'LineWidth', 2);
set(gcf,'color','white');
set(gcf, 'Position', [600 400 700 500]);
hold on

subplot(2, 1, 2);
h2 = semilogx(idx2, avg_fans_statuses_ki, '--o', 'LineWidth', 1, 'Color', [0, 0.45, 0.74], 'MarkerSize', 10, 'MarkerEdgeColor', [0, 0.45, 0.74], 'MarkerFaceColor', [0, 0.45, 0.74]);
xlabel('$K_{i}$', 'interpreter', 'Latex');
ylabel('$fans\_statuses$', 'interpreter', 'Latex');
% legend(h2, 'ki\_statuses\_count', 'location', 'NE');
set(gca, 'FontSize', 18);
set(gca, 'LineWidth', 2);
set(gcf,'color','white');
set(gcf, 'Position', [600 400 700 500]);

