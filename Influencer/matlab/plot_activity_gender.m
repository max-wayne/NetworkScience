function plot_activity_gender()
s = 'D:\Projects\Pycharm\BIGV\data';
s1 = strcat(s, '\bigv\gender');
gender = load(s1);
ki = gender(:, 2); ko = gender(:, 3);

A1 = []; A2 = []; E1 = []; E2 = [];
idx = [];
%--ki(0:14), ko(18:27)
for i = 18 : 27
    idx = [idx 2^i];
end
for j = 1 : length(idx)-1
    id = find(gender(:, 3)>=idx(j) & gender(:, 3)<idx(j+1));
    avg_male = mean(gender(id, 4));
    var_male = sum((gender(id, 4)-avg_male).^2) / length(id);
    avg_female = mean(gender(id, 5));
    var_female = sum((gender(id, 5)-avg_male).^2) / length(id);
    A1 = [A1 avg_male]; E1 = [E1 sqrt(var_male)];
    A2 = [A2 avg_female]; E2 = [E2 sqrt(var_female)];
end
figure(1);
h1 = semilogx(idx(2:end-1), A1(1:end-1), '--b.', 'LineWidth', 2, 'MarkerSize', 50);
hold on;
errorbar(idx(2:end-1), A1(1:end-1), E1(1:end-1), -E1(1:end-1), 'Marker', 's', 'Color', [.5, .5, .5], 'LineWidth', 2, 'LineStyle', 'none');
h2 = semilogx(idx(2:end-1), A2(1:end-1), '--r.', 'LineWidth', 2, 'MarkerSize', 50);
errorbar(idx(2:end-1), A2(1:end-1), E2(1:end-1), -E2(1:end-1), 'Marker', 's', 'Color', [.5, .5, .5], 'LineWidth', 2, 'LineStyle', 'none');
xlabel('$K_{o}$', 'interpreter', 'latex');
ylabel('$Ratio$', 'interpreter', 'latex');
L1 = legend([h1, h2], ...
        'male', ...
        'female', ...
        'location', 'SE');
xlim([300000, 1e8]);
set(gca, 'FontSize', 18);
set(gca, 'LineWidth', 2);
set(gcf,'color','white');
set(gcf, 'Position', [600 400 700 500]);
set(L1, 'FontSize', 12);

A1 = []; A2 = []; E1 = []; E2 = [];
idx = [];
for i = 0 : 14
    idx = [idx 2^i];
end
for j = 1 : length(idx)-1
    id = find(gender(:, 2)>=idx(j) & gender(:, 2)<idx(j+1));
    avg_male = mean(gender(id, 4));
    var_male = sum((gender(id, 4)-avg_male).^2) / length(id);
    avg_female = mean(gender(id, 5));
    var_female = sum((gender(id, 5)-avg_male).^2) / length(id);
    A1 = [A1 avg_male]; E1 = [E1 sqrt(var_male)];
    A2 = [A2 avg_female]; E2 = [E2 sqrt(var_female)];
end
figure(2);
h3 = semilogx(idx(2:end-2), A1(1:end-2), '--b.', 'LineWidth', 2, 'MarkerSize', 50);
hold on;
errorbar(idx(2:end-2), A1(1:end-2), E1(1:end-2), -E1(1:end-2), 'Marker', 's', 'Color', [.5, .5, .5], 'LineWidth', 2, 'LineStyle', 'none');
h4 = semilogx(idx(2:end-2), A2(1:end-2), '--r.', 'LineWidth', 2, 'MarkerSize', 50);
errorbar(idx(2:end-2), A2(1:end-2), E2(1:end-2), -E2(1:end-2), 'Marker', 's', 'Color', [.5, .5, .5], 'LineWidth', 2, 'LineStyle', 'none');
xlabel('$K_{i}$', 'interpreter', 'latex');
ylabel('$Ratio$', 'interpreter', 'latex');
L2 = legend([h3, h4], ...
        'male', ...
        'female', ...
        'location', 'SE');
set(gca, 'XTick', [1e1, 1e2, 1e3, 1e4]);
set(gca, 'FontSize', 18);
set(gca, 'LineWidth', 2);
set(gcf,'color','white');
set(gcf, 'Position', [600 400 700 500]);
set(L1, 'FontSize', 12);


