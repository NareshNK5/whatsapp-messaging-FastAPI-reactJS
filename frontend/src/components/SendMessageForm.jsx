import { useState } from 'react';
import axios from 'axios';

function SendMessageForm() {
  const [phone, setPhone] = useState('');
  const [status, setStatus] = useState('');

  const handleSend = async () => {
    try {
      const res = await axios.get(`http://localhost:8000/send_message`, {
        params: { phone_number: phone },
      });
      setStatus(res.data.message);
    } catch (err) {
      setStatus(err.response?.data?.detail || 'Something went wrong');
    }
  };

  return (
    <div>
      <input
        placeholder="+14155552671"
        value={phone}
        onChange={(e) => setPhone(e.target.value)}
      />
      <button onClick={handleSend}>Send Message</button>
      <p>{status}</p>
    </div>
  );
}

export default SendMessageForm;
