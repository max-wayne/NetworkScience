clear; clc;
load('D:\double_check\info\stat_results\see_order');
load('D:\double_check\info\stat_results\ret_order');
%% Plot
M_see = zeros(337, 1200); M_ret = zeros(337, 1000); 
see_unret = see_order(:, 1:1000) - ret_order(:, 1:1000);
M_see_unret = zeros(337, 1000);
for i = 1 : 337
    M_see(i, :) = see_order(i, :) / sum(see_order(i, :));
    M_ret(i, :) = ret_order(i, :) / sum(ret_order(i, :));
    M_see_unret(i, :) = see_unret(i, :) / sum(see_unret(i, :));
end
A = mean(M_see); B = mean(M_ret); C = mean(M_see_unret);
figure; bar(A(1:20)); 
figure; bar(B(1:20));
figure; bar(C(1:20));


