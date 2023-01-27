import React, { useState, useEffect } from "react";
import axios from "axios";
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';

const APISearch = () => {
  const [name, setName] = useState("");
  const [APIs, setAPIs] = useState({});

  useEffect(() => {
    const searchAPIs = async () => {
      console.log("searchAPIs")
      const res = await axios.get("http://localhost:5000/search", {
        params: {
          name: name
        }
      });
      setAPIs(res.data.hits.hits);
    };
    if (name) {
      searchAPIs();
    } else {
      setAPIs([]);
    }
  }, [name]);

  return (
    <div>
      <form>
        <label>
          API Name
          <input type="text" value={name} onChange={event => setName(event.target.value)} />
        </label>
        <br />
      </form>
      <div>
      {APIs && 
      <Tabs>
        <TabList>
          <Tab>StackOverflow</Tab>
          <Tab>GitHub</Tab>
          <Tab>Tweet</Tab>
          <Tab>CVE</Tab>
          <Tab>YouTube</Tab>
        </TabList>

        <TabPanel>
          <div>
            {"stackoverflow" in APIs && APIs["stackoverflow"].map(API => (
              <div class="border" key={API._id}>
                <p><b>Title</b><br/>{API._source.title}</p>
                <p><b>Link</b><br/> {API._source.link}</p>
                <p><b>Content</b><br/>{API._source.content}</p>
              </div>
            ))}
          </div>
        </TabPanel>

        <TabPanel>
          <div>
              {"github" in APIs && APIs["github"].map(API => (
                <div class="border" key={API._id}>
                  <p><b>Content</b><br/>{API._source.content}</p>
                </div>
              ))}
          </div>
        </TabPanel>


        <TabPanel>
          <div>
              {"tweet" in APIs && APIs["tweet"].map(API => (
                <div class="border" key={API._id}>
                  <p><b>Content</b><br/>{API._source.content}</p>
                </div>
              ))}
          </div>
        </TabPanel>

        <TabPanel>
          <div>
              {"cve" in APIs && APIs["cve"].map(API => (
                <div class="border" key={API._id}>
                  <p><b>Content</b><br/>{API._source.content}</p>
                </div>
              ))}
          </div>
        </TabPanel>

        <TabPanel>
          <div>
              {"youtube" in APIs && APIs["youtube"].map(API => (
                <div class="border" key={API._id}>
                  <p><b>Content</b><br/>{API._source.content}</p>
                </div>
              ))}
          </div>
        </TabPanel>
      </Tabs>
      }
      </div>
    </div>
  );
};





export default APISearch;
