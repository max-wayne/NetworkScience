function plot_urank_dist()
s = 'D:/Projects/Pycharm/BIGV/data/bigv/ko_urank/';
figure(1);
for i = 18 : 25
    s1 = strcat(s, num2str(i));
    data1 = load(s1);
    tbl1 = tabulate(data1);
    T1 = tbl1(:, 3) / 100;
    h1 = plot(T1, '--o', 'LineWidth', 1, 'MarkerSize', 8);
    hold on
end
xlabel('$User Rank$', 'interpreter', 'latex');
ylabel('$Ratio$', 'interpreter', 'latex');
L1 = legend(h1, 'different kout', 'location', 'NE');
set(L1, 'box', 'off', 'Fontname', 'Times New Roman', 'FontSize', 20);
set(gca,'XTick',[0 5 10 15 20 30 40 50]);
set(gca, 'FontSize', 18);
set(gca, 'LineWidth', 2);
set(gcf,'color','white');
set(gcf, 'Position', [600 400 700 500]);


t = 'D:/Projects/Pycharm/BIGV/data/bigv/ki_urank/';
figure(2);
for j = 0 : 12
    t1 = strcat(t, num2str(j));
    data2 = load(t1);
    tbl2 = tabulate(data2);
    T2 = tbl2(:, 3) / 100;
    h2 = plot(T2, '--o', 'LineWidth', 1, 'MarkerSize', 8);
    hold on
end
xlabel('$User Rank$', 'interpreter', 'latex');
ylabel('$Ratio$', 'interpreter', 'latex');
L2 = legend(h2, 'different kin', 'location', 'NE');
set(L2, 'box', 'off', 'Fontname', 'Times New Roman', 'FontSize', 20);
set(gca,'XTick',[0 5 10 15 20 30 40 50]);
set(gca, 'FontSize', 18);
set(gca, 'LineWidth', 2);
set(gcf,'color','white');
set(gcf, 'Position', [600 400 700 500]);