<ul>
  <li><b>Start Azure VM (ubuntu) </b>  </li>
  <li><b>Login to Your Azure VM</b>
    <p>Login to your Azure VM using SSH with the following command:</p>
    <pre><code>ssh -i azurebob.pem azureuserbob@52.140.99.173</code></pre>
  </li>
  <li><b>Copy Files to Your Azure VM</b>
    <p>Copy the necessary files from the "Azure-VM-files" directory on your local machine to any location in the VM using SCP. Replace <code>&lt;filename&gt;</code> with the name of the file you want to copy and <code>&lt;destination_path&gt;</code> with the path where you want to copy the file to.</p>
    <pre><code>scp /Azure-VM-files/&lt;filename&gt; azureuserbob@52.140.99.173:/&lt;destination_path&gt;</code></pre>
  </li>
  <li><b>Run the Script</b>
    <p>Before running the script, ensure that the script files have the correct permissions. Change the permissions of the <code>.sh</code> files using the following commands:</p>
    <pre><code>chmod +x script.sh
chmod +x run.sh</code></pre>
    <p>Now, you can run the script from your VM using:</p>
    <pre><code>sh run.sh</code></pre>
  </li>
  <li><b>View in your browser</b>
    <p>To make the flask server accessible from anywhere, configure Azure VM Network Security Group (NSG).<br>
      You need to open port 5000 on your Azure VM's Network Security Group (NSG) to allow inbound traffic.<br>
      Go to the Azure Portal:<br>
      ->Navigate to your VM's resource group.<br>
      ->Click on the Network Security Group associated with your VM.<br>
      ->Add an Inbound Security Rule:<br>
      ->Click on "Inbound security rules".<br>
      ->Click on "Add".<br>
      ->Configure the rule as follows:<br>
      ->Source: Any<br>
      ->Source port ranges: *<br>
      ->Destination: Any<br>
      ->Destination port ranges: 5000<br>
      ->Protocol: TCP<br>
      ->Action: Allow<br>
      ->Priority: Set a value (e.g., 1000)<br>
      ->Name: Allow-5000<br>
      ->Click on "Add" to save the rule.</p>
    <p>Now, on running the server, it should be accessible from anywhere using the public ip of the VM (The Public IP Address can be found in the "Overview" page of the VM in Azure Portal. </p>
    Example <code>http://52.140.99.173:5000/</code>
  </li>
</ul>

### Prerequisites
<code>python 3.9</code><br>
<code>wireshark/Tshark in the Azure VM</code><br>
<code>Flask, scapy, tensorflow, scikit-learn, pandas, xgboost, shap. </code> <i>Use <code>pip install <package_name></code></i><br>

### Thank You
