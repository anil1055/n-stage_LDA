# n-stage Latent Dirichlet Allocation (n-LDA)
Proposed n-LDA & A Novel Approach for classical LDA: related paper <https://arxiv.org/abs/2110.08591>

Latent Dirichlet Allocation (LDA) is a generative probabilistic topic model for a given text collection. Topics have a probability distribution over words and text documents over topics. Each subject has a probability distribution over the fixed word corpus [1]. The method exemplifies a mix of these topics for each document. Then, a model is produced by sampling words from this mixture [2].

The coherence value, which is the topic modeling criterion, is used to determine the number of K topic in the system. The coherence value calculates the closeness of words to each other. The topic value of the highest one among the calculated consistency values is chosen as the topic number of the system [3].

After modeling the system with classical LDA, an LDA-based n-stage method is proposed to increase the success of the model. The value of n in the method may vary according to the size of the dataset. With the method, it is aimed to delete the words in the corpus that negatively affect the success. Thus, with the increase in the weight values of the words in the topics formed with the remaining words, the class labels of the topics can be determined more easily [4].

![image](https://user-images.githubusercontent.com/17703776/137033562-ead3d00b-7c42-445e-ab22-5ab272357ef6.png)

The steps of the method are shown in above Figure. In order to reduce the number of words in the dictionary, the threshold value for each topic is calculated. The threshold value is obtained by dividing the sum of the weights of all the words to the word count in the relevant topic. Words with a weight less than the specified threshold value are deleted from the topics and a new dictionary is created for the model. Finally, the system is re-modeled using the LDA algorithm with the new dictionary. These steps can be repeated n times [4].

This method was applied for Turkish and English language. n-stage LDA method was better than classic LDA according to related studies. 

# Related papers & articles for n-stage LDA

!!! Please citation this paper: 
```
@article{guven2020comparison,
  title={Comparison of n-stage Latent Dirichlet Allocation versus other topic modeling methods for emotion analysis},
  author={G{\"u}ven, Zekeriya An{\i}l and Diri, Banu and {\c{C}}akalo{\u{g}}lu, Tolgahan},
  journal={Journal of the Faculty of Engineering and Architecture of Gazi University},
  volume={35},
  number={4},
  pages={2135--2146},
  year={2020},
  doi={10.17341/gazimmfd.556104}
}
```

1-Guven, Z. A., Diri, B., & Cakaloglu, T. (2018, October). Classification of New Titles by Two Stage Latent Dirichlet Allocation. In 2018 Innovations in Intelligent Systems and Applications Conference (ASYU) (pp. 1-5). Ieee.

2-Guven, Z. A., Diri, B., & Cakaloglu, T. (2021). Evaluation of Non-Negative Matrix Factorization and n-stage Latent Dirichlet Allocation for Emotion Analysis in Turkish Tweets. arXiv preprint arXiv:2110.00418.

3-Güven, Z. A., Diri, B., & Çakaloğlu, T. (2020). Comparison of n-stage Latent Dirichlet Allocation versus other topic modeling methods for emotion analysis. Journal of the Faculty of Engineering and Architecture of Gazi University, 35(4), 2135-2146.

4-Güven, Z. A., Diri, B., & Çakaloğlu, T. (2018, April). Classification of TurkishTweet emotions by n-stage Latent Dirichlet Allocation. In 2018 Electric Electronics, Computer Science, Biomedical Engineerings' Meeting (EBBT) (pp. 1-4). IEEE.

5-Güven, Z. A., Diri, B., & Çakaloğlu, T. (2019, September). Comparison of Topic Modeling Methods for Type Detection of Turkish News. In 2019 4th International Conference on Computer Science and Engineering (UBMK) (pp. 150-154). IEEE.

6-GÜVEN, Z. A., Banu, D. İ. R. İ., & ÇAKALOĞLU, T. (2019). Emotion Detection with n-stage Latent Dirichlet Allocation for Turkish Tweets. Academic Platform Journal of Engineering and Science, 7(3), 467-472.

7-Güven, Z. A., Diri, B., & Çakaloğlu, T. Comparison Method for Emotion Detection of Twitter Users. In 2019 Innovations in Intelligent Systems and Applications Conference (ASYU) (pp. 1-5). IEEE.


# References

[1] David M. Blei, Andrew Y. Ng, and Michael I. Jordan.  Latent Dirichlet allocation.Journal of Machine LearningResearch, 2003. ISSN 15324435. doi:10.1016/b978-0-12-411519-4.00006-9.

[2] Yong  Chen,  Hui  Zhang,  Rui  Liu,  Zhiwen  Ye,  and  Jianying  Lin.Experimental  explorations  on  short  texttopic  mining  between  LDA  and  NMF  based  Schemes.Knowledge-Based Systems,  2019.    ISSN  09507051.doi:10.1016/j.knosys.2018.08.011.

[3] Zekeriya Anil Güven, Banu Diri, and Tolgahan Çakaloˇglu. Classification of New Titles by Two Stage Latent DirichletAllocation. InProceedings - 2018 Innovations in Intelligent Systems and Applications Conference, ASYU 2018, 2018.ISBN 9781538677865. doi:10.1109/ASYU.2018.8554027.

[4] Guven, Zekeriya Anil, Banu Diri, and Tolgahan Cakaloglu. "Evaluation of Non-Negative Matrix Factorization and n-stage Latent Dirichlet Allocation for Emotion Analysis in Turkish Tweets." arXiv preprint arXiv:2110.00418 (2021).

