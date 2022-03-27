        <Sensor>
          <Description>Nanometrics Trillium Compact 120 (Vault, Posthole, OBS)</Description>
        </Sensor>
        <Response>
          <InstrumentSensitivity>
            <Value>316872887.761</Value>
            <Frequency>1.0</Frequency>
            <InputUnits>
              <Name>M/S</Name>
              <Description>Velocity in Meters per Second</Description>
            </InputUnits>
            <OutputUnits>
              <Name>COUNTS</Name>
              <Description>Digital Counts</Description>
            </OutputUnits>
          </InstrumentSensitivity>
          <Stage number="1">
            <PolesZeros>
              <InputUnits>
                <Name>M/S</Name>
                <Description>Velocity in Meters per Second</Description>
              </InputUnits>
              <OutputUnits>
                <Name>V</Name>
                <Description>Volts</Description>
              </OutputUnits>
              <PzTransferFunctionType>LAPLACE (RADIANS/SECOND)</PzTransferFunctionType>
              <NormalizationFactor>4.344928e+17</NormalizationFactor>
              <NormalizationFrequency unit="HERTZ">1.0</NormalizationFrequency>
              <Zero number="0">
                <Real minusError="0.0" plusError="0.0">0.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Zero>
              <Zero number="1">
                <Real minusError="0.0" plusError="0.0">0.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Zero>
              <Zero number="2">
                <Real minusError="-392.0" plusError="-392.0">-392.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Zero>
              <Zero number="3">
                <Real minusError="-1960.0" plusError="-1960.0">-1960.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Zero>
              <Zero number="4">
                <Real minusError="-1490.0" plusError="-1490.0">-1490.0</Real>
                <Imaginary minusError="1740.0" plusError="1740.0">1740.0</Imaginary>
              </Zero>
              <Zero number="5">
                <Real minusError="-1490.0" plusError="-1490.0">-1490.0</Real>
                <Imaginary minusError="-1740.0" plusError="-1740.0">-1740.0</Imaginary>
              </Zero>
              <Pole number="0">
                <Real minusError="-0.03691" plusError="-0.03691">-0.03691</Real>
                <Imaginary minusError="0.03702" plusError="0.03702">0.03702</Imaginary>
              </Pole>
              <Pole number="1">
                <Real minusError="-0.03691" plusError="-0.03691">-0.03691</Real>
                <Imaginary minusError="-0.03702" plusError="-0.03702">-0.03702</Imaginary>
              </Pole>
              <Pole number="2">
                <Real minusError="-343.0" plusError="-343.0">-343.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Pole>
              <Pole number="3">
                <Real minusError="-370.0" plusError="-370.0">-370.0</Real>
                <Imaginary minusError="467.0" plusError="467.0">467.0</Imaginary>
              </Pole>
              <Pole number="4">
                <Real minusError="-370.0" plusError="-370.0">-370.0</Real>
                <Imaginary minusError="-467.0" plusError="-467.0">-467.0</Imaginary>
              </Pole>
              <Pole number="5">
                <Real minusError="-836.0" plusError="-836.0">-836.0</Real>
                <Imaginary minusError="1522.0" plusError="1522.0">1522.0</Imaginary>
              </Pole>
              <Pole number="6">
                <Real minusError="-836.0" plusError="-836.0">-836.0</Real>
                <Imaginary minusError="-1522.0" plusError="-1522.0">-1522.0</Imaginary>
              </Pole>
              <Pole number="7">
                <Real minusError="-4900.0" plusError="-4900.0">-4900.0</Real>
                <Imaginary minusError="4700.0" plusError="4700.0">4700.0</Imaginary>
              </Pole>
              <Pole number="8">
                <Real minusError="-4900.0" plusError="-4900.0">-4900.0</Real>
                <Imaginary minusError="-4700.0" plusError="-4700.0">-4700.0</Imaginary>
              </Pole>
              <Pole number="9">
                <Real minusError="-6900.0" plusError="-6900.0">-6900.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Pole>
              <Pole number="10">
                <Real minusError="-15000.0" plusError="-15000.0">-15000.0</Real>
                <Imaginary minusError="0.0" plusError="0.0">0.0</Imaginary>
              </Pole>
            </PolesZeros>
            <StageGain>
              <Value>754.3</Value>
              <Frequency>1.0</Frequency>
            </StageGain>
          </Stage>
          <Stage number="2">
            <StageGain>
              <Value>1.0</Value>
              <Frequency>0.02</Frequency>
            </StageGain>
          </Stage>
          <Stage number="3">
            <Coefficients>
              <InputUnits>
                <Name>V</Name>
                <Description>Volts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </OutputUnits>
              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
              <Numerator>1.0</Numerator>
            </Coefficients>
            <Decimation>
              <InputSampleRate unit="HERTZ">30000.0</InputSampleRate>
              <Factor>1</Factor>
              <Offset>0</Offset>
              <Delay>0.0</Delay>
              <Correction>0.0</Correction>
            </Decimation>
            <StageGain>
              <Value>420168.0</Value>
              <Frequency>0.02</Frequency>
            </StageGain>
          </Stage>
          <Stage number="4">
            <Coefficients>
              <InputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </OutputUnits>
              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
              <Numerator>8.48249e-06</Numerator>
              <Numerator>3.89037e-05</Numerator>
              <Numerator>0.000109346</Numerator>
              <Numerator>0.000226937</Numerator>
              <Numerator>0.00036584</Numerator>
              <Numerator>0.000447944</Numerator>
              <Numerator>0.000346227</Numerator>
              <Numerator>-7.08089e-05</Numerator>
              <Numerator>-0.000851525</Numerator>
              <Numerator>-0.00185801</Numerator>
              <Numerator>-0.0027055</Numerator>
              <Numerator>-0.00281272</Numerator>
              <Numerator>-0.00160384</Numerator>
              <Numerator>0.00116656</Numerator>
              <Numerator>0.00508161</Numerator>
              <Numerator>0.00890325</Numerator>
              <Numerator>0.010758</Numerator>
              <Numerator>0.00873375</Numerator>
              <Numerator>0.00177379</Numerator>
              <Numerator>-0.00943683</Numerator>
              <Numerator>-0.0219989</Numerator>
              <Numerator>-0.0310883</Numerator>
              <Numerator>-0.0311164</Numerator>
              <Numerator>-0.0175223</Numerator>
              <Numerator>0.0113614</Numerator>
              <Numerator>0.0530733</Numerator>
              <Numerator>0.100994</Numerator>
              <Numerator>0.145714</Numerator>
              <Numerator>0.177481</Numerator>
              <Numerator>0.188975</Numerator>
              <Numerator>0.177481</Numerator>
              <Numerator>0.145714</Numerator>
              <Numerator>0.100994</Numerator>
              <Numerator>0.0530733</Numerator>
              <Numerator>0.0113614</Numerator>
              <Numerator>-0.0175223</Numerator>
              <Numerator>-0.0311164</Numerator>
              <Numerator>-0.0310883</Numerator>
              <Numerator>-0.0219989</Numerator>
              <Numerator>-0.00943683</Numerator>
              <Numerator>0.00177379</Numerator>
              <Numerator>0.00873375</Numerator>
              <Numerator>0.010758</Numerator>
              <Numerator>0.00890325</Numerator>
              <Numerator>0.00508161</Numerator>
              <Numerator>0.00116656</Numerator>
              <Numerator>-0.00160384</Numerator>
              <Numerator>-0.00281272</Numerator>
              <Numerator>-0.0027055</Numerator>
              <Numerator>-0.00185801</Numerator>
              <Numerator>-0.000851525</Numerator>
              <Numerator>-7.08089e-05</Numerator>
              <Numerator>0.000346227</Numerator>
              <Numerator>0.000447944</Numerator>
              <Numerator>0.00036584</Numerator>
              <Numerator>0.000226937</Numerator>
              <Numerator>0.000109346</Numerator>
              <Numerator>3.89037e-05</Numerator>
              <Numerator>8.48249e-06</Numerator>
            </Coefficients>
            <Decimation>
              <InputSampleRate unit="HERTZ">30000.0</InputSampleRate>
              <Factor>5</Factor>
              <Offset>0</Offset>
              <Delay>0.0009666667</Delay>
              <Correction>0.0009666667</Correction>
            </Decimation>
            <StageGain>
              <Value>1.0</Value>
              <Frequency>0.02</Frequency>
            </StageGain>
          </Stage>
          <Stage number="5">
            <Coefficients>
              <InputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </OutputUnits>
              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
              <Numerator>4.13e-05</Numerator>
              <Numerator>0.000235</Numerator>
              <Numerator>0.000591</Numerator>
              <Numerator>0.000653</Numerator>
              <Numerator>-0.000476</Numerator>
              <Numerator>-0.00295</Numerator>
              <Numerator>-0.00455</Numerator>
              <Numerator>-0.00124</Numerator>
              <Numerator>0.00811</Numerator>
              <Numerator>0.0164</Numerator>
              <Numerator>0.0105</Numerator>
              <Numerator>-0.0155</Numerator>
              <Numerator>-0.0454</Numerator>
              <Numerator>-0.0428</Numerator>
              <Numerator>0.0223</Numerator>
              <Numerator>0.141</Numerator>
              <Numerator>0.259</Numerator>
              <Numerator>0.308</Numerator>
              <Numerator>0.259</Numerator>
              <Numerator>0.141</Numerator>
              <Numerator>0.0223</Numerator>
              <Numerator>-0.0428</Numerator>
              <Numerator>-0.0454</Numerator>
              <Numerator>-0.0155</Numerator>
              <Numerator>0.0105</Numerator>
              <Numerator>0.0164</Numerator>
              <Numerator>0.00811</Numerator>
              <Numerator>-0.00124</Numerator>
              <Numerator>-0.00455</Numerator>
              <Numerator>-0.00295</Numerator>
              <Numerator>-0.000476</Numerator>
              <Numerator>0.000653</Numerator>
              <Numerator>0.000591</Numerator>
              <Numerator>0.000235</Numerator>
              <Numerator>4.13e-05</Numerator>
            </Coefficients>
            <Decimation>
              <InputSampleRate unit="HERTZ">6000.0</InputSampleRate>
              <Factor>3</Factor>
              <Offset>0</Offset>
              <Delay>0.002833333</Delay>
              <Correction>0.002833333</Correction>
            </Decimation>
            <StageGain>
              <Value>1.0</Value>
              <Frequency>0.02</Frequency>
            </StageGain>
          </Stage>
          <Stage number="6">
            <Coefficients>
              <InputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </OutputUnits>
              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
              <Numerator>-1.25729e-08</Numerator>
              <Numerator>-1.05239e-07</Numerator>
              <Numerator>-4.85219e-07</Numerator>
              <Numerator>-1.62749e-06</Numerator>
              <Numerator>-4.36278e-06</Numerator>
              <Numerator>-9.75467e-06</Numerator>
              <Numerator>-1.85249e-05</Numerator>
              <Numerator>-2.98359e-05</Numerator>
              <Numerator>-3.95435e-05</Numerator>
              <Numerator>-3.85744e-05</Numerator>
              <Numerator>-1.27601e-05</Numerator>
              <Numerator>5.41867e-05</Numerator>
              <Numerator>0.000173287</Numerator>
              <Numerator>0.00033889</Numerator>
              <Numerator>0.000516461</Numerator>
              <Numerator>0.000635812</Numerator>
              <Numerator>0.000597759</Numerator>
              <Numerator>0.000300498</Numerator>
              <Numerator>-0.000314192</Numerator>
              <Numerator>-0.00120507</Numerator>
              <Numerator>-0.00218704</Numerator>
              <Numerator>-0.00292612</Numerator>
              <Numerator>-0.00299796</Numerator>
              <Numerator>-0.0020174</Numerator>
              <Numerator>0.000182455</Numerator>
              <Numerator>0.003375</Numerator>
              <Numerator>0.00684425</Numerator>
              <Numerator>0.00944234</Numerator>
              <Numerator>0.00984065</Numerator>
              <Numerator>0.00695227</Numerator>
              <Numerator>0.00042907</Numerator>
              <Numerator>-0.00892353</Numerator>
              <Numerator>-0.0189876</Numerator>
              <Numerator>-0.026559</Numerator>
              <Numerator>-0.0279847</Numerator>
              <Numerator>-0.020103</Numerator>
              <Numerator>-0.0012493</Numerator>
              <Numerator>0.0279692</Numerator>
              <Numerator>0.0644083</Numerator>
              <Numerator>0.10278</Numerator>
              <Numerator>0.136674</Numerator>
              <Numerator>0.159965</Numerator>
              <Numerator>0.168261</Numerator>
              <Numerator>0.159965</Numerator>
              <Numerator>0.136674</Numerator>
              <Numerator>0.10278</Numerator>
              <Numerator>0.0644083</Numerator>
              <Numerator>0.0279692</Numerator>
              <Numerator>-0.0012493</Numerator>
              <Numerator>-0.020103</Numerator>
              <Numerator>-0.0279847</Numerator>
              <Numerator>-0.026559</Numerator>
              <Numerator>-0.0189876</Numerator>
              <Numerator>-0.00892353</Numerator>
              <Numerator>0.00042907</Numerator>
              <Numerator>0.00695227</Numerator>
              <Numerator>0.00984065</Numerator>
              <Numerator>0.00944234</Numerator>
              <Numerator>0.00684425</Numerator>
              <Numerator>0.003375</Numerator>
              <Numerator>0.000182455</Numerator>
              <Numerator>-0.0020174</Numerator>
              <Numerator>-0.00299796</Numerator>
              <Numerator>-0.00292612</Numerator>
              <Numerator>-0.00218704</Numerator>
              <Numerator>-0.00120507</Numerator>
              <Numerator>-0.000314192</Numerator>
              <Numerator>0.000300498</Numerator>
              <Numerator>0.000597759</Numerator>
              <Numerator>0.000635812</Numerator>
              <Numerator>0.000516461</Numerator>
              <Numerator>0.00033889</Numerator>
              <Numerator>0.000173287</Numerator>
              <Numerator>5.41867e-05</Numerator>
              <Numerator>-1.27601e-05</Numerator>
              <Numerator>-3.85744e-05</Numerator>
              <Numerator>-3.95435e-05</Numerator>
              <Numerator>-2.98359e-05</Numerator>
              <Numerator>-1.85249e-05</Numerator>
              <Numerator>-9.75467e-06</Numerator>
              <Numerator>-4.36278e-06</Numerator>
              <Numerator>-1.62749e-06</Numerator>
              <Numerator>-4.85219e-07</Numerator>
              <Numerator>-1.05239e-07</Numerator>
              <Numerator>-1.25729e-08</Numerator>
            </Coefficients>
            <Decimation>
              <InputSampleRate unit="HERTZ">2000.0</InputSampleRate>
              <Factor>5</Factor>
              <Offset>0</Offset>
              <Delay>0.021</Delay>
              <Correction>0.021</Correction>
            </Decimation>
            <StageGain>
              <Value>1.0</Value>
              <Frequency>0.02</Frequency>
            </StageGain>
          </Stage>
          <Stage number="7">
            <Coefficients>
              <InputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </InputUnits>
              <OutputUnits>
                <Name>COUNTS</Name>
                <Description>Digital Counts</Description>
              </OutputUnits>
              <CfTransferFunctionType>DIGITAL</CfTransferFunctionType>
              <Numerator>0.000112421</Numerator>
              <Numerator>0.00123518</Numerator>
              <Numerator>0.00687794</Numerator>
              <Numerator>0.0254743</Numerator>
              <Numerator>0.0694733</Numerator>
              <Numerator>0.146035</Numerator>
              <Numerator>0.240282</Numerator>
              <Numerator>0.30568</Numerator>
              <Numerator>0.2828</Numerator>
              <Numerator>0.148674</Numerator>
              <Numerator>-0.0404598</Numerator>
              <Numerator>-0.167739</Numerator>
              <Numerator>-0.145516</Numerator>
              <Numerator>-0.00410536</Numerator>
              <Numerator>0.120323</Numerator>
              <Numerator>0.110823</Numerator>
              <Numerator>-0.0107507</Numerator>
              <Numerator>-0.105917</Numerator>
              <Numerator>-0.0726648</Numerator>
              <Numerator>0.039929</Numerator>
              <Numerator>0.0935874</Numerator>
              <Numerator>0.029149</Numerator>
              <Numerator>-0.0647119</Numerator>
              <Numerator>-0.068577</Numerator>
              <Numerator>0.0151868</Numerator>
              <Numerator>0.0717562</Numerator>
              <Numerator>0.0294078</Numerator>
              <Numerator>-0.0482479</Numerator>
              <Numerator>-0.0547218</Numerator>
              <Numerator>0.013358</Numerator>
              <Numerator>0.0576458</Numerator>
              <Numerator>0.0190461</Numerator>
              <Numerator>-0.0428831</Numerator>
              <Numerator>-0.0400759</Numerator>
              <Numerator>0.0187966</Numerator>
              <Numerator>0.0465427</Numerator>
              <Numerator>0.00605678</Numerator>
              <Numerator>-0.039946</Numerator>
              <Numerator>-0.0251628</Numerator>
              <Numerator>0.0246829</Numerator>
              <Numerator>0.0350373</Numerator>
              <Numerator>-0.00617551</Numerator>
              <Numerator>-0.0352079</Numerator>
              <Numerator>-0.0106559</Numerator>
              <Numerator>0.0275344</Numerator>
              <Numerator>0.0223679</Numerator>
              <Numerator>-0.0152164</Numerator>
              <Numerator>-0.0273885</Numerator>
              <Numerator>0.00178073</Numerator>
              <Numerator>0.0259161</Numerator>
              <Numerator>0.00974328</Numerator>
              <Numerator>-0.0194773</Numerator>
              <Numerator>-0.0173472</Numerator>
              <Numerator>0.0103164</Numerator>
              <Numerator>0.0202358</Numerator>
              <Numerator>-0.000780326</Numerator>
              <Numerator>-0.0187303</Numerator>
              <Numerator>-0.00718083</Numerator>
              <Numerator>0.0139675</Numerator>
              <Numerator>0.0123234</Numerator>
              <Numerator>-0.00750047</Numerator>
              <Numerator>-0.0142117</Numerator>
              <Numerator>0.000901851</Numerator>
              <Numerator>0.0131357</Numerator>
              <Numerator>0.00455291</Numerator>
              <Numerator>-0.00990145</Numerator>
              <Numerator>-0.00807528</Numerator>
              <Numerator>0.00556306</Numerator>
              <Numerator>0.00941565</Numerator>
              <Numerator>-0.00116201</Numerator>
              <Numerator>-0.00879668</Numerator>
              <Numerator>-0.00247475</Numerator>
              <Numerator>0.00676654</Numerator>
              <Numerator>0.00484982</Numerator>
              <Numerator>-0.00401918</Numerator>
              <Numerator>-0.00581909</Numerator>
              <Numerator>0.00122524</Numerator>
              <Numerator>0.00553916</Numerator>
              <Numerator>0.00109395</Numerator>
              <Numerator>-0.0043665</Numerator>
              <Numerator>-0.00263378</Numerator>
              <Numerator>0.00273874</Numerator>
              <Numerator>0.00331145</Numerator>
              <Numerator>-0.0010741</Numerator>
              <Numerator>-0.00324038</Numerator>
              <Numerator>-0.00033628</Numerator>
              <Numerator>0.00259506</Numerator>
              <Numerator>0.0012372</Numerator>
              <Numerator>-0.00174961</Numerator>
              <Numerator>-0.00172252</Numerator>
              <Numerator>0.000805307</Numerator>
              <Numerator>0.00174012</Numerator>
              <Numerator>-9.85432e-06</Numerator>
              <Numerator>-0.00143607</Numerator>
              <Numerator>-0.000522671</Numerator>
              <Numerator>0.000983023</Numerator>
              <Numerator>0.000784544</Numerator>
              <Numerator>-0.000515897</Numerator>
              <Numerator>-0.000822884</Numerator>
              <Numerator>0.000122716</Numerator>
              <Numerator>0.000708811</Numerator>
              <Numerator>0.000153361</Numerator>
              <Numerator>-0.000515633</Numerator>
              <Numerator>-0.000305407</Numerator>
              <Numerator>0.000304889</Numerator>
              <Numerator>0.00035103</Numerator>
              <Numerator>-0.000119475</Numerator>
              <Numerator>-0.000320522</Numerator>
              <Numerator>-1.74777e-05</Numerator>
              <Numerator>0.000246918</Numerator>
              <Numerator>9.97921e-05</Numerator>
              <Numerator>-0.00015904</Numerator>
              <Numerator>-0.000133325</Numerator>
              <Numerator>7.77561e-05</Numerator>
              <Numerator>0.000130585</Numerator>
              <Numerator>-1.50176e-05</Numerator>
              <Numerator>-0.000106015</Numerator>
              <Numerator>-2.50954e-05</Numerator>
              <Numerator>7.25999e-05</Numerator>
              <Numerator>4.42336e-05</Numerator>
              <Numerator>-3.99733e-05</Numerator>
              <Numerator>-4.73149e-05</Numerator>
              <Numerator>1.38576e-05</Numerator>
              <Numerator>4.03496e-05</Numerator>
              <Numerator>3.53809e-06</Numerator>
              <Numerator>-2.88561e-05</Numerator>
              <Numerator>-1.25761e-05</Numerator>
              <Numerator>1.69775e-05</Numerator>
              <Numerator>1.51051e-05</Numerator>
              <Numerator>-7.20657e-06</Numerator>
              <Numerator>-1.3486e-05</Numerator>
              <Numerator>5.57862e-07</Numerator>
              <Numerator>9.90881e-06</Numerator>
              <Numerator>3.03239e-06</Numerator>
              <Numerator>-6.00796e-06</Numerator>
              <Numerator>-4.23333e-06</Numerator>
              <Numerator>2.75811e-06</Numerator>
              <Numerator>3.9232e-06</Numerator>
              <Numerator>-5.48083e-07</Numerator>
              <Numerator>-2.9006e-06</Numerator>
              <Numerator>-6.39819e-07</Numerator>
              <Numerator>1.74996e-06</Numerator>
              <Numerator>1.04913e-06</Numerator>
              <Numerator>-8.01869e-07</Numerator>
              <Numerator>-9.8208e-07</Numerator>
              <Numerator>1.79745e-07</Numerator>
              <Numerator>7.06408e-07</Numerator>
              <Numerator>1.3737e-07</Numerator>
              <Numerator>-4.02797e-07</Numerator>
              <Numerator>-2.32831e-07</Numerator>
              <Numerator>1.68104e-07</Numerator>
              <Numerator>2.06754e-07</Numerator>
              <Numerator>-2.6077e-08</Numerator>
              <Numerator>-1.34576e-07</Numerator>
              <Numerator>-3.44589e-08</Numerator>
              <Numerator>6.65896e-08</Numerator>
              <Numerator>4.56348e-08</Numerator>
              <Numerator>-1.95578e-08</Numerator>
              <Numerator>-3.3062e-08</Numerator>
              <Numerator>-1.86265e-09</Numerator>
              <Numerator>1.72295e-08</Numerator>
              <Numerator>8.3819e-09</Numerator>
              <Numerator>-4.65661e-09</Numerator>
              <Numerator>-6.0536e-09</Numerator>
              <Numerator>0.0</Numerator>
              <Numerator>3.25963e-09</Numerator>
              <Numerator>2.32831e-09</Numerator>
              <Numerator>4.65661e-10</Numerator>
              <Numerator>0.0</Numerator>
              <Numerator>0.0</Numerator>
              <Numerator>0.0</Numerator>
              <Numerator>0.0</Numerator>
              <Numerator>0.0</Numerator>
            </Coefficients>
            <Decimation>
              <InputSampleRate unit="HERTZ">400.0</InputSampleRate>
              <Factor>2</Factor>
              <Offset>0</Offset>
              <Delay>0.021</Delay>
              <Correction>0.021</Correction>
            </Decimation>
            <StageGain>
              <Value>1.0</Value>
              <Frequency>0.02</Frequency>
            </StageGain>
          </Stage>
        </Response>