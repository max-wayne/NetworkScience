function plot_activity()
s = 'D:\Projects\Pycharm\BIGV\data';
s1 = strcat(s, '\bigv\activity_2018_07_01');
activity = load(s1);
ki = activity(:, 2); ko = activity(:, 3);
A = []; E = [];
idx = [];
%--ki(0:14), ko(18:27)
for i = 18 : 27
    idx = [idx 2^i];
end
for j = 1 : length(idx)-1
    id = find(activity(:, 3)>idx(j) & activity(:, 3)<idx(j+1));
    avg_value = mean(activity(id, 4));
    var_value = sum((activity(id, 4)-avg_value).^2) / length(id);
    A = [A avg_value];
    E = [E sqrt(var_value)];
end
figure;
subplot(1, 2, 1);
semilogx(idx(2:end-1), A(1:end-1), '--b.', 'LineWidth', 2, 'MarkerSize', 50);
% errorbar(idx(2:end-1), A(1:end-1), E(1:end-1), -E(1:end-1), 'Marker', 's', 'Color', [.5, .5, .5], 'LineWidth', 2, 'LineStyle', 'none');
xlabel('$K_{o}$', 'interpreter', 'latex');
ylabel('$Activity$', 'interpreter', 'latex');
xlim([300000, 1e8]);
ylim([0.3, 0.4]);
set(gca, 'FontSize', 18);
set(gca, 'LineWidth', 2);
set(gcf,'color','white');
set(gcf, 'Position', [600 400 700 500]);
hold on;

A = []; E = [];
idx = []; N = [];
for i = 0 : 14
    idx = [idx 2^i];
end
for j = 1 : length(idx)-1
    id = find(activity(:, 2)>=idx(j) & activity(:, 2)<idx(j+1));
    N = [N length(id)];
    avg_value = mean(activity(id, 4));
    var_value = sum((activity(id, 4)-avg_value).^2) / length(id);
    A = [A avg_value];
    E = [E sqrt(var_value)];
end

subplot(1, 2, 2);
semilogx(idx(2:end-2), A(1:end-2), '--r.', 'LineWidth', 2, 'MarkerSize', 50);
% errorbar(idx(2:end-2), A(1:end-2), E(1:end-2), -E(1:end-2), 'Marker', 's', 'Color', [.5, .5, .5], 'LineWidth', 2, 'LineStyle', 'none');
xlabel('$K_{i}$', 'interpreter', 'latex');
ylabel('$Activity$', 'interpreter', 'latex');
set(gca, 'XTick', [1e1, 1e2, 1e3, 1e4]);
set(gca, 'FontSize', 18);
set(gca, 'LineWidth', 2);
set(gcf,'color','white');
set(gcf, 'Position', [600 400 800 500]);

