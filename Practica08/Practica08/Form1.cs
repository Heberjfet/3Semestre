using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO.Ports;

namespace Practica08
{
    public partial class Form1 : Form
    {
        delegate void SetTextDelegate(string value);

        public SerialPort ArduinoPort { 
            get;
        }

        public Form1()
        {
            InitializeComponent();
            ArduinoPort = new System.IO.Ports.SerialPort();
            ArduinoPort.PortName = "COM5"; // Check on your machine
            ArduinoPort.BaudRate = 9600;
            ArduinoPort.DataBits = 8;
            ArduinoPort.ReadTimeout = 500;
            ArduinoPort.WriteTimeout = 500;
            ArduinoPort.DataReceived += new SerialDataReceivedEventHandler(DataReceivedHandler);
            ArduinoPort.Open(); // Uncomment this if you want to open the port

            // Bind events
            this.Conectar.Click += btnConectar_Click;
        }

        private void DataReceivedHandler(object sender, SerialDataReceivedEventArgs e)
        {
            string data = ArduinoPort.ReadLine();
            WriteToTxt(data);
        }

        private void WriteToTxt(string data)
        {
            if (InvokeRequired)
            {
                try
                {
                    Invoke(new SetTextDelegate(WriteToTxt), new object[] { data });
                }
                catch { }
            }
            else
            {
                lbTemp.Text = data;
            }
        }

        private void btnConectar_Click(object sender, EventArgs e)
        {
            Desconectar.Enabled = true;
            //Conectar.Enabled = false;

            try
            {
                if (!ArduinoPort.IsOpen)
                {
                    ArduinoPort.Open();
                }

                if (int.TryParse(tbLimit.Text, out int temperatureLimit)) // Assuming tbLimit is the TextBox for the temperature limit
                {
                    // Convert the value to a string and then to a byte array
                    string limitString = temperatureLimit.ToString();
                    ArduinoPort.Write(limitString);
                }
                else
                {
                    MessageBox.Show("Please enter a valid numeric value in the TextBox for the temperature limit.");
                }

                lbConnection.Text = "Connection OK";
                lbConnection.ForeColor = System.Drawing.Color.Lime;
            }
            catch
            {
                MessageBox.Show("Please check your communication port or disconnect.");
            }
        }

        private void btnDesconectar_Click(object sender, EventArgs e)
        {
            Conectar.Enabled = true;
            Desconectar.Enabled = false;

            if (ArduinoPort.IsOpen)
                ArduinoPort.Close();

            lbConnection.Text = "Disconnected";
            lbConnection.ForeColor = System.Drawing.Color.Red;
            lbTemp.Text = "00.0";
        }
    }
}
