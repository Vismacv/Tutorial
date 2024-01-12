import anova
import chi_squretest
import coefficentrange
import KPcorrelation
import mean
import median
import mode
import stat_range
import SEofMean
import SEofStandardDeviation
import SRank_withoutR
import SRank_withR
import standard_deviation
import t_test
import variance

anva=anova.ANOVA([11.6,10.3,10,11.5,11.8,9],[9,12,14,15.5,14],[7,12,15,18,15])

chi=chi_squretest.chi_squre([56,18,31,6],[58,16,29,8])

corange=coefficentrange.Co_range([60,70,80,100,120,140,200])

kPcorln=KPcorrelation.correlation([102,101,100,99,96],[100,90,80,70,60])

mn=mean.Mean([2,3,4,5])

mdn=median.Median([5,6,3,8,1])
 
mod=mode.Mode([1,2,4,1,4,7,4])

rng=stat_range.Range([4,6,9,10,8,3])

semean=SEofMean.SEMean([2,5,3,4,1])

sesd=SEofStandardDeviation.SEofSD([2,5,3,4,1])

sprmnwout=SRank_withoutR.Rank([1,4,8,9,3],[4,8,7,4,6])

sprmnwr=SRank_withR.rank([1,4,8,9,3],[4,8,7,4,6])

sd=standard_deviation.SD([4,6,8,7])

ttest=t_test.t_Test([49,41,45,43,48],[52,51,45,48,50])

vrince=variance.Variance([5,4,7,8,9])






