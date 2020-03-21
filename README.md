## cvd-19-experiments
----------------------
(a) clone the data-set [repository](https://github.com/CSSEGISandData/COVID-19) locally from JHU (our scripts will pull the latest data everytime) 
.  
(b) clone [this](https://github.com/anishacharya/cvd-19-experiments) repository in the same folder(for relative path consistency in config).  
(c) run <code>sh driver.sh "country(Optional)| default=US"</code>   

### Sample setup
-------------------
<pre>
git clone https://github.com/CSSEGISandData/COVID-19.git   
git clone https://github.com/anishacharya/cvd-19-experiments.git   
cd cvd-19-experiments   
sh driver.sh 'China'              
</pre>
