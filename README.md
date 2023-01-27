# Google-IT-Automation-with-Python-Professional-Certificate
"Automating Real-World Tasks with Python" My solutions for the last 4 challenges of the last course. 

All 4 final qwiklabs were quite challenging and interesting and allowed me to use the skills I learned throughout the course, also challenge myself to find solutions to unexpected problems that were not necessarily specified in the qwiklabs but that came up. 

It may serve to clarify everything was done using a linux server VM, no GUI except for the visualization of websites. 

<h1>First week challenge</h1>

<ul>
  
  Using the PIL library and more
  
  <li>Convert all files in a directory from TIFF to JPEG</li>
  <li>Resize all .jpeg images</li>
  <li>Rotate each Image 90 degrees, move them all to a new directory (used shutil library)</li>
</ul>

<h1>Second week challenge</h1>

<ul>
  
  In an environment created in Google qwiklabs there was a django server configured. We had to use os, requests, and json libraries. Will also upload some testing scripts using before creating the final "run.py"
  
  <li>Create valid JSON from txt files stored in a directory</li>
  <li>Send that JSON to the pre configured django website </li>

</ul>

<h1>Third week challenge</h1>

<ul>
  
  For this week's challenge we had to use the ReportLab module to generate PDFs. We also used smtp and mimetypes in order to be able to send emails with attachments using python scripts. Some of the scripts were prebuilt, and we had to put the missing pieces together and create the necessary missing scripts. We had to:
  
  <li>Calculate the most popular year of sales by year of multiple car brands and models (popular_car_year.py)</li>
  <li>Exctract relevant data from a JSON file (cleaning data)</li>
  <li>Create final PDF report </li>
  <li>Send email with generated PDF as attachment (sender, receiver, subject, body, attachment) (cars.py)</li>
</ul>

<h1>Fourth (final) week challenge</h1>

<ul>
  
  This was the longest challenge, quite interesting indeed. Must admit it took me quite longer than the 2 hours of the qwiklab.
  Main goaisl were to combine everything learned up to this point
  
  <li>Dowload and extract files into the server using a provided .sh script files included images and .txt files</li>
  <li>Creating a script to resize all images and convert them to JPEG</li>
  <li>Upload all images into the bre configured server (django)</li>
  <li>Go through the directory that had the .txt files, read each one of them, and create valid JSON out of them</li>
  <li>Appending the corresponding .JPEG image to the txt file before processing the JSON, this was kind of an extra challenge on itself. To solve this i used the (add_img_names.py) script</li>
  <li>Sending the processed correct JSON into the server in order to upload the fruits catalog</li>
  <li>Generating a PDF report of the fruit catalog, extracting only name and weight, send it via email.<li/>
  <li>Perform a health check of the system including CPU, Disk Space, RAM, and hostname. Auto send email if tresholds were detected. This was tested using the linux stress test program (sudo apt install stress)<li/>

</ul>

<h1>Bonus script: touchpy</h1>

I will also include a "bonus_script" that is a script I created to create python and bash scripts, and even files in other programming languages. The python and bash scripts are created with the shebang included and permissions to execute (not 777). This code was created when I was doing the first courses, and I discovered it can be improved, so I will be working to update it and add new features. I think it is a relevant script as it has helped me a lot throughout the entire specialization and for every python and bash script I make.  I named it "touchpy". 

