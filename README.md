# Bayesian mutual info

_Mutual information_ is an interesting quantity that can be used to eg. measure the relatedness of two words in a corpus. It's defined as

$$
\log \frac{p(x,y)}{p(x)p(y)} = \log \frac{p(y \mid x)}{p(y)} 
$$

In order to get a Bayesian estimate for the mutual information, we want to model two quantities

$$
\begin{aligned}
p(y \mid x) &= \rho \\
p(y) &= \lambda
\end{aligned}
$$

To simplify things a bit, we will treat the two quantities as independent. In that case, it is relatively simple to model $\lambda$. We'll use a flat prior (though a Dirichlet based on the number of classes would also do), and use the Binomial likelihood. The flat prior yields the posterior 

$$
\lambda \sim \text{Beta}(Y + 1, N - Y + 1)
$$

where $Y$ is the number of times the word $y$ appears in the data, and $N$ is the length of the dataset.

A reasonable prior for $\rho$ would be the posterior distribution for $\lambda$. A priori, $\rho$ thus follows

$$
\rho \sim \text{Beta}(Y + 1, N - Y + 1)
$$

Adding the data for the co-occurences, we obtain a posterior

$$
\rho \sim \text{Beta}(Y + Y^\prime + 1, N - Y - Y^\prime + - X \cdot W + 1)
$$

where $Y^\prime$ is the number of times the word $y$ occures in the same word window as $x$, $X$ is the number of times word $x$ appears in the data, and $W$ is the window size.

The mutual information requires the calculation of the expectation

$$
\begin{aligned}
E[\log \frac{p(y \mid x)}{p(y)} \\
&= E[\log \frac{\rho}{\lambda}
&= E[\log (\rho)] - E[\log(\lambda) ]
\end{aligned}
$$

This has the closed form solution

$$
E[\log (\rho)] - E[\log(\lambda) ] = \digamma(\alpha_\rho) - \digamma(\alpha_\rho + \beta_\rho) - \digamma(\alpha_\lambda) + \digamma(\alpha_\lambda + \beta_\lambda)
$$