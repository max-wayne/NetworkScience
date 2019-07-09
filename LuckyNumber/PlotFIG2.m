clear; clc;
figure;
ha = tight_subplot(1, 2,[.05 .08],[.25 .1],[.15 .1]);
set(gcf,'color','white');
set(gcf, 'Position', [500 300 800 500]);

axes(ha(1));
load('./data/posts.txt');
x=posts(:, 2); y=posts(:, 3);
h1=semilogx(posts(:,1), x/sum(x), '-', 'LineWidth', 3, 'Color', [0, 0.75, 0.75]); 
hold on;
h2=semilogx(posts(:,1), y/sum(y), '-', 'LineWidth', 3, 'Color', [0.87, 0.49, 0]);
xlabel('Number of posts'); ylabel('Distribution');
legend([h1, h2], {'with preference', 'without preference'}, 'location', 'NE');
ylim([0 0.16]);
set(legend, 'box', 'off', 'FontName', 'Times New Roman', 'FontSize', 15);
set(gca, 'box', 'on', 'LineWidth', 1.5, 'FontName', 'Times New Roman', 'FontSize',18);

axes(ha(2));
load('./data/follower.txt');
x=follower(:,2); y=follower(:,3);
semilogx(follower(:,1), x/sum(x), '-', 'LineWidth', 3, 'Color', [0, 0.75, 0.75]); 
hold on;
semilogx(follower(:,1), y/sum(y), '-', 'LineWidth', 3, 'Color', [0.87, 0.49, 0]);
xlabel('Number of followers');
set(gca, 'YTick', [0, 0.01, 0.03, 0.05, 0.07], 'YTickLabel', {'0', '0.01', '0.03', '0.05', '0.07'});
set(gca, 'box', 'on', 'LineWidth', 1.5, 'FontName', 'Times New Roman', 'FontSize',18);




