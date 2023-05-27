[generation_id, win_rates, chromosome] = importfile('agn_10_gms_200_gen_500_mut_0.1_mutS_0.1_el_0.1.csv');
close all
fig = figure;
plot(min(win_rates,[],2))
hold on
plot(mean(win_rates,2))
plot(max(win_rates,[],2))
xlabel('Generation')
ylabel('Win rate')
legend(["min","mean","max"],"Location","southeast")
grid on
title("Mut rate: %, Mut size: %")
set(gcf,'units','points','position',[500,500,200,150])


