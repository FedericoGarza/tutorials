# Applications

This is a list of examples of Fugue applications. Any questions are welcome in the Slack channel.

[![Slack Status](https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social)](https://join.slack.com/t/fugue-project/shared_invite/zt-jl0pcahu-KdlSOgi~fP50TZWmNxdWYQ)


```{toctree}
:hidden:

data_validation
testing
databricks_connect
coiled
```

## [Data Validation](data_validation.ipynb)
We'll get started with using Fugue and Pandera for data validation. Using Fugue, we can bring Pandas-based libraries into Spark, meaning we don't have to re-implement the same logic twice. Moreover, using Fugue allows us to achieve **validation by partition**, an operation missing in the current data validation frameworks.

## [Testing Big Data Applications](testing.ipynb)
Unit testing is a significant pain point in big data applications. In this section, we examine what makes it so hard to test and how Fugue simplifies it. Through simplified testing, Fugue users often see speedup in the development of big data projects (in addition to lower compute costs).

## Using Fugue with Providers

Since Fugue is a framework for distributed compute, it is often paired with a solution that manages Spark or Dask clusters. This section will cover how to use Fugue with different providers.

### [Fugue and Databricks Connect](databricks_connect.ipynb)
Fugue can be used with the `databricks-connect` library to run code that uses the `SparkExecutionEngine` on a Databricks cluster. Here we'll go over some details of how to set it up.

### [Fugue and Coiled](coiled.ipynb)
Coiled is one of the leading solutions to manage Dask clusters. Here, we go over how to spin up a Dask cluster with Coiled and use Fugue on the cluster.