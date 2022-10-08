import React, { useState } from "react";
import { FaMicrophone } from "react-icons/fa";
import {BiChevronDown} from "react-icons/bi";
import {FaStopCircle} from "react-icons/fa";
import { ReactMediaRecorder } from "react-media-recorder";

function Dropdown() {
  
  const [isOpen, setIsOpen] = useState(false);
  return (
    <div className="">    
      
      <section
        className="pt-px pb-20 bg-gray-900 my-0 text-gray-300"
      >
        <div className="container mx-auto px-4">
          <div className="flex flex-wrap items-center mt-32">
            <div className="lg:pt-1 pt-0 w-full md:w-5/12 px-4 mr-auto ml-auto">
              {/* <!-- <div class="text-gray-600 p-3 text-center inline-flex items-center justify-center w-16 h-16 mb-6 shadow-lg rounded-full bg-gray-100"></div> --> */}
              <h1 className="text-6xl mb-2 font-semibold leading-normal">
                Amahric News
              </h1>
              <div className="w-96 font-medium h-20 text-gray-900">
                <div className="bg-white w-full p-2 flex items-center justify-between rounded">
                  select news
                  <BiChevronDown size={20} />
                </div>
                <ul className="bg-white mt-2 hidden">
                  <li className="p-2 text-sm hover:bg-blue-600 hover:text-white">Sports</li>
                  <li className="p-2 text-sm hover:bg-blue-600 hover:text-white">Local</li>
                </ul>
              </div>
              <button class="place-content-center text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2.5 text-center inline-flex items-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800 mb-10" type="button">Generate</button>
              <p className="text-lg font-light leading-relaxed mt-0 mb-4 text-gray-400">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Quas libero laudantium non asperiores pariatur iusto consequatur provident! Maiores ut, officia non minus, quaerat quidem voluptatibus at reiciendis, voluptates molestiae ullam?
              </p>
              <div className="place-items-center">
                
                <ReactMediaRecorder 
                  audio
                  render={({ status, startRecording, stopRecording, mediaBlobUrl }) => (
                    <div>
                      <p>{status}</p>
                      <button onClick={startRecording} className="bg-blue-600 rounded-full text-gray-300 hover:bg-gray-300 hover:text-blue-600 text-sm px-4 py-2.5 text-center"><FaMicrophone size={20}/></button>
                      <button onClick={stopRecording} className="bg-red-600 rounded-full text-gray-300 hover:bg-gray-300 hover:text-red-600 text-sm px-4 py-2.5 text-center"><FaStopCircle size={20}/></button>
                      <video src={mediaBlobUrl} controls autoPlay loop />
                    </div>
                  )} 
                />
              </div>
               <p> </p>
            </div>
          </div>
        </div>
      </section>
      
    </div>
  );

}
export default Dropdown;
