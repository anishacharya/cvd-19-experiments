### Sample setup
-------------------
(a) clone the data-set [repository](https://github.com/CSSEGISandData/COVID-19) locally from JHU (our scripts will pull the latest data everytime) 
.  
(b) clone [this](https://github.com/anishacharya/cvd-19-experiments) repository in the same folder(for relative path consistency in config).  
<pre>
git clone https://github.com/CSSEGISandData/COVID-19.git   
git clone https://github.com/anishacharya/cvd-19-experiments.git   
cd cvd-19-experiments                
</pre>

### Example Usage
------------------- 
<pre>
sh driver.sh US new
sh driver.sh Japan cum
sh driver.sh China new bar 
sh driver.sh India cum line  
</pre>



