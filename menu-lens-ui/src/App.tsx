// React + React-Bootstrap + Tesseract + SerpApi MVP
// Structure: Single page app with OCR + image search

import React, { useState } from 'react';
import { Container, Row, Col, Form, Button, Card, Spinner } from 'react-bootstrap';
import Tesseract from 'tesseract.js';

const App = () => {
  const [imageFile, setImageFile] = useState(null);
  const [dishNames, setDishNames] = useState([]);
  const [dishImages, setDishImages] = useState({});
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setImageFile(e.target.files[0]);
  };

  const handleProcessImage = async () => {
    if (!imageFile) return;
    setLoading(true);

    const {
      data: { text },
    } = await Tesseract.recognize(imageFile, 'eng');

    const lines = text
      .split('\n')
      .map((line) => line.trim())
      .filter((line) => line.length > 1);

    setDishNames(lines);
    fetchDishImages(lines);
  };

  const fetchDishImages = async (names) => {
    const apiKey = ''//'0e0037a700ed31b63ca15633bbc1cf621e35314743ec0bb8ddce67417e0e1a5c'; // Replace with your key
    const results = {};

    for (const name of names) {
      try {
        const res = await fetch(
          `https://serpapi.com/search.json?q=${encodeURIComponent(
            name + ' food'
          )}&tbm=isch&api_key=${apiKey}`
        );
        const data = await res.json();
        results[name] = data.images_results?.[0]?.thumbnail || '';
      } catch (error) {
        results[name] = '';
      }
    }

    setDishImages(results);
    setLoading(false);
  };

  return (
    <Container className="p-4">
      <h2 className="mb-4">Visual Menu Scanner</h2>
      <Form.Group controlId="formFile" className="mb-3">
        <Form.Label>Upload Menu Image</Form.Label>
        <Form.Control type="file" onChange={handleFileChange} accept="image/*" />
      </Form.Group>
      <Button variant="primary" onClick={handleProcessImage} disabled={loading}>
        {loading ? <Spinner animation="border" size="sm" /> : 'Scan Menu'}
      </Button>

      <Row className="mt-4">
        {dishNames.map((dish, idx) => (
          <Col md={4} className="mb-4" key={idx}>
            <Card>
              {dishImages[dish] ? (
                <Card.Img variant="top" src={dishImages[dish]} />
              ) : (
                <Card.Img
                  variant="top"
                  src="https://via.placeholder.com/300x200?text=No+Image"
                />
              )}
              <Card.Body>
                <Card.Title>{dish}</Card.Title>
              </Card.Body>
            </Card>
          </Col>
        ))}
      </Row>
    </Container>
  );
};

export default App;
